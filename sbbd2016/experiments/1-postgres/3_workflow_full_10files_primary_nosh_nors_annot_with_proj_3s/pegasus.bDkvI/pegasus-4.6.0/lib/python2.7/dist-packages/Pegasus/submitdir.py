import os
import glob
import tarfile
import shutil
import logging
from optparse import OptionParser


from Pegasus.db import connection
from Pegasus.tools import utils
from Pegasus.command import LoggingCommand, CompoundCommand
from Pegasus.db.schema import *

log = logging.getLogger(__name__)

class SubmitDirException(Exception): pass

class MainDatabase:
    def __init__(self, session):
        self.session = session

    def get_main_workflow(self, wf_uuid):
        q = self.session.query(DashboardWorkflow)
        q = q.filter(DashboardWorkflow.wf_uuid == wf_uuid)
        wf = q.first()
        return wf

    def get_ensemble_workflow(self, wf_uuid):
        q = self.session.query(EnsembleWorkflow)
        q = q.filter(EnsembleWorkflow.wf_uuid == wf_uuid)
        return q.first()

    def delete_main_workflow(self, wf_uuid):
        w = self.get_main_workflow(wf_uuid)
        if w is None:
            return

        # Delete any ensemble workflows
        q = self.session.query(EnsembleWorkflow)
        q = q.filter(EnsembleWorkflow.wf_uuid == wf_uuid)
        q.delete()

        # Delete the workflow
        q = self.session.query(DashboardWorkflow)
        q = q.filter(DashboardWorkflow.wf_id == w.wf_id)
        q.delete()

class WorkflowDatabase(object):
    def __init__(self, session):
        self.session = session

    def delete_workflow(self, wf_uuid):
        q = self.session.query(Workflow)
        q = q.filter(Workflow.wf_uuid == wf_uuid)
        w = q.first()

        # If not found, do nothing
        if w is None:
            log.warning("Workflow not found in workflow DB: %s" % wf_uuid)
            return

        # Delete it
        self.session.delete(w)

    def get_workflow(self, wf_uuid):
        q = self.session.query(Workflow)
        q = q.filter(Workflow.wf_uuid == wf_uuid)
        return q.first()

    def get_workflow_states(self, wf_id):
        q = self.session.query(Workflowstate)
        q = q.filter(Workflowstate.wf_id == wf_id)
        return q.all()

    def update_submit_dirs(self, root_wf_id, src, dest):
        q = self.session.query(Workflow)
        q = q.filter(Workflow.root_wf_id == root_wf_id)
        for wf in q.all():
            log.info("Old submit dir: %s" % wf.submit_dir)
            wf.submit_dir = wf.submit_dir.replace(src, dest)
            log.info("New submit dir: %s" % wf.submit_dir)

class SubmitDir(object):
    def __init__(self, submitdir):
        if not os.path.isdir(submitdir):
            raise SubmitDirException("Invalid submit dir: %s" % submitdir)
        self.submitdir = os.path.abspath(submitdir)

        # Locate braindump file
        self.braindump_file = os.path.join(self.submitdir, "braindump.txt")
        if not os.path.isfile(self.braindump_file):
            raise SubmitDirException("Not a submit directory: braindump.txt missing")

        # Read the braindump file
        self.braindump = utils.read_braindump(self.braindump_file)

        # Read some attributes from braindump file
        self.wf_uuid = self.braindump["wf_uuid"]
        self.root_wf_uuid = self.braindump["root_wf_uuid"]
        self.user = self.braindump["user"]

        self.archname = os.path.join(self.submitdir, "archive.tar.gz")

    def is_subworkflow(self):
        "Check to see if this workflow is a subworkflow"
        return self.wf_uuid != self.root_wf_uuid

    def is_archived(self):
        "A submit dir is archived if the archive file exists"
        return os.path.isfile(self.archname)

    def extract(self):
        "Extract files from an archived submit dir"

        # Locate archive file
        if not self.is_archived():
            raise SubmitDirException("Submit dir not archived")

        # Update record in main db
        mdbsession = connection.connect_by_submitdir(self.submitdir, connection.DBType.MASTER)
        mdb = MainDatabase(mdbsession)
        wf = mdb.get_main_workflow(self.wf_uuid)
        if wf is not None:
            wf.archived = False

        # Untar the files
        tar = tarfile.open(self.archname, "r:gz")
        tar.extractall(path=self.submitdir)
        tar.close()

        # Remove the tar file
        os.remove(self.archname)

        # Commit the workflow changes
        mdbsession.commit()
        mdbsession.close()

    def archive(self):
        "Archive a submit dir by adding files to a compressed archive"

        # Update record in main db
        mdbsession = connection.connect_by_submitdir(self.submitdir, connection.DBType.MASTER)
        mdb = MainDatabase(mdbsession)
        wf = mdb.get_main_workflow(self.wf_uuid)
        if wf is not None:
            wf.archived = True

        # The set of files to exclude from the archive
        exclude = set()

        # Exclude braindump file
        exclude.add(self.braindump_file)

        # We use a temporary file so that we can determine if the archive step
        # completed successfully later
        tmparchname = os.path.join(self.submitdir, "archive.tmp.tar.gz")

        # We use a lock file to determine if cleanup is complete
        lockfile = os.path.join(self.submitdir, "archive.cleanup.lock")

        # If a previous archive was partially completed, then remove the
        # temporary file that was created
        if os.path.exists(tmparchname):
            os.unlink(tmparchname)

        # Exclude the temporary archive name so we don't add it to itself
        exclude.add(tmparchname)

        # We don't want the lock file to be saved, if it exists
        exclude.add(lockfile)

        # Also exclude the final archive name in case they try to run it again
        exclude.add(self.archname)

        # Ignore monitord files. This is needed so that tools like pegasus-statistics
        # will consider the workflow to be complete
        for name in ["monitord.started", "monitord.done", "monitord.log"]:
            exclude.add(os.path.join(self.submitdir, name))

        # Exclude stampede db
        for db in glob.glob(os.path.join(self.submitdir, "*.stampede.db")):
            exclude.add(db)

        # Exclude properties file
        for prop in glob.glob(os.path.join(self.submitdir, "pegasus.*.properties")):
            exclude.add(prop)

        # Visit all the files in the submit dir that we want to archive
        def visit(dirpath):
            for name in os.listdir(dirpath):
                filepath = os.path.join(dirpath, name)

                if filepath not in exclude:
                    yield name, filepath

        if self.is_archived() and not os.path.exists(lockfile):
            raise SubmitDirException("Submit directory already archived")

        if not self.is_archived():
            # Archive the files
            print "Creating archive..."
            tar = tarfile.open(name=tmparchname, mode="w:gz")
            for name, path in visit(self.submitdir):
                tar.add(name=path, arcname=name)
            tar.close()

            # This "commits" the archive step
            os.rename(tmparchname, self.archname)

        # Touch lockfile
        open(lockfile, "w").close()

        # Remove the files and directories
        # We do this here, instead of doing it in the loop above
        # because we want to make sure there are no errors in creating
        # the archive before we start removing files
        print "Removing files..."
        for name, path in visit(self.submitdir):
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
            else:
                shutil.rmtree(path)

        # This "commits" the file removal
        os.unlink(lockfile)

        # Commit the workflow changes
        mdbsession.commit()
        mdbsession.close()

    def move(self, dest):
        "Move this submit directory to dest"

        dest = os.path.abspath(dest)

        if os.path.isfile(dest):
            raise SubmitDirException("Destination is a file: %s" % dest)

        if os.path.isdir(dest):
            if os.path.exists(os.path.join(dest, "braindump.txt")):
                raise SubmitDirException("Destination is a submit dir: %s" % dest)
            dest = os.path.join(dest, os.path.basename(self.submitdir))

        # Verify that we aren't trying to move a subworkflow
        if self.is_subworkflow():
            raise SubmitDirException("Subworkflows cannot be moved independent of the root workflow")

        # Connect to main database
        mdbsession = connection.connect_by_submitdir(self.submitdir, connection.DBType.MASTER)
        mdb = MainDatabase(mdbsession)

        # Get the workflow record from the main db
        db_url = None
        wf = mdb.get_main_workflow(self.wf_uuid)
        if wf is None:
            db_url = connection.url_by_submitdir(self.submitdir, connection.DBType.WORKFLOW)
        else:
            # We found an mdb record, so we need to update it

            # Save the main db's pointer
            db_url = wf.db_url

            # Update the main db's db_url
            # Note that this will only update the URL if it is an sqlite file
            # located in the submitdir
            log.info("Old main db_url: %s" % wf.db_url)
            wf.db_url = db_url.replace(self.submitdir, dest)
            log.info("New main db_url: %s" % wf.db_url)

            # Change the main db's submit_dir
            log.info("Old main submit_dir: %s" % wf.submit_dir)
            wf.submit_dir = dest
            log.info("New main submit_dir: %s" % wf.submit_dir)

        # Update the ensemble record if one exists
        ew = mdb.get_ensemble_workflow(self.wf_uuid)
        if ew is not None:
            log.info("Old ensemble submit dir: %s", ew.submitdir)
            ew.submitdir = dest
            log.info("New ensemble submit dir: %s", ew.submitdir)

        # Update the workflow database if we found one
        if db_url is not None:
            dbsession = connection.connect(db_url)
            db = WorkflowDatabase(dbsession)
            root_wf = db.get_workflow(self.wf_uuid)
            db.update_submit_dirs(root_wf.wf_id, self.submitdir, dest)
            dbsession.commit()
            dbsession.close()

        # Move all the files
        shutil.move(self.submitdir, dest)

        # Set new paths in the braindump file
        self.braindump["submit_dir"] = dest
        self.braindump["basedir"] = os.path.dirname(dest)
        utils.write_braindump(os.path.join(dest, "braindump.txt"), self.braindump)

        # Note that we do not need to update the properties file even though it
        # might contain DB URLs because it cannot contain a DB URL with the submit
        # dir in it.

        # TODO We might want to update all of the absolute paths in the condor submit files
        # if we plan on moving workflows that could be resubmitted in the future

        # TODO We might want to update the braindump files for subworkflows

        # Update main database
        mdbsession.commit()
        mdbsession.close()

        # Finally, update object
        self.submitdir = dest

    def delete(self):
        "Delete this submit dir and its entry in the main db"

        # Verify that we aren't trying to move a subworkflow
        if self.is_subworkflow():
            raise SubmitDirException("Subworkflows cannot be deleted independent of the root workflow")

        # Confirm that they want to delete the workflow
        while True:
            sys.stdout.write("Are you sure you want to delete this workflow? This operation cannot be undone. [y/n]: ")
            answer = raw_input().strip().lower()
            if answer == "y":
                break
            if answer == "n":
                return

        # Connect to main database
        mdbsession = connection.connect_by_submitdir(self.submitdir, connection.DBType.MASTER)
        mdb = MainDatabase(mdbsession)

        # Delete all of the records from the workflow db if they are not using
        # an sqlite db that is in the submit dir.
        db_url = connection.url_by_submitdir(self.submitdir, connection.DBType.WORKFLOW)
        if self.submitdir not in db_url:
            dbsession = connection.connect(db_url)
            db = WorkflowDatabase(dbsession)
            db.delete_workflow(self.wf_uuid)
            dbsession.commit()
            dbsession.close()

        # Delete the workflow
        mdb.delete_main_workflow(self.wf_uuid)

        # Remove all the files
        shutil.rmtree(self.submitdir)

        # Update main db
        mdbsession.commit()
        mdbsession.close()

    def attach(self):
        "Add a workflow to the main db"

        # Verify that we aren't trying to attach a subworkflow
        if self.is_subworkflow():
            raise SubmitDirException("Subworkflows cannot be attached independent of the root workflow")

        # Connect to main database
        mdbsession = connection.connect_by_submitdir(self.submitdir, connection.DBType.MASTER)
        mdb = MainDatabase(mdbsession)

        # Check to see if it already exists and just update it
        wf = mdb.get_main_workflow(self.wf_uuid)
        if wf is not None:
            print "Workflow is already in main db"
            old_submit_dir = wf.submit_dir
            if old_submit_dir != self.submitdir:
                print "Updating path..."
                wf.submit_dir = self.submitdir
                wf.db_url = connection.url_by_submitdir(self.submitdir, connection.DBType.WORKFLOW)
                mdbsession.commit()
            mdbsession.close()
            return

        # Connect to workflow db
        db_url = connection.url_by_submitdir(self.submitdir, connection.DBType.WORKFLOW)
        dbsession = connection.connect(db_url)
        db = WorkflowDatabase(dbsession)

        # Get workflow record
        wf = db.get_workflow(self.wf_uuid)
        if wf is None:
            print "No database record for that workflow exists"
            return

        # Update the workflow record
        wf.submit_dir = self.submitdir
        wf.db_url = db_url

        # Insert workflow record into main db
        mwf = DashboardWorkflow()
        mwf.wf_uuid = wf.wf_uuid
        mwf.dax_label = wf.dax_label
        mwf.dax_version = wf.dax_version
        mwf.dax_file = wf.dax_file
        mwf.dag_file_name = wf.dag_file_name
        mwf.timestamp = wf.timestamp
        mwf.submit_hostname = wf.submit_hostname
        mwf.submit_dir = self.submitdir
        mwf.planner_arguments = wf.planner_arguments
        mwf.user = wf.user
        mwf.grid_dn = wf.grid_dn
        mwf.planner_version = wf.planner_version
        mwf.db_url = wf.db_url
        mwf.archived = self.is_archived()
        mdbsession.add(mwf)
        mdbsession.flush() # We should have the new wf_id after this

        # Query states from workflow database
        states = db.get_workflow_states(wf.wf_id)

        # Insert states into main db
        for s in states:
            ms = DashboardWorkflowstate()
            ms.wf_id = mwf.wf_id
            ms.state = s.state
            ms.timestamp = s.timestamp
            ms.restart_count = s.restart_count
            ms.status = s.status
            mdbsession.add(ms)
        mdbsession.flush()

        dbsession.commit()
        dbsession.close()

        mdbsession.commit()
        mdbsession.close()

    def detach(self):
        "Remove any main db entries for the given root workflow"

        # Verify that we aren't trying to detach a subworkflow
        if self.is_subworkflow():
            raise SubmitDirException("Subworkflows cannot be detached independent of the root workflow")

        # Connect to main database
        mdbsession = connection.connect_by_submitdir(self.submitdir, connection.DBType.MASTER)
        mdb = MainDatabase(mdbsession)

        # Check to see if it even exists
        wf = mdb.get_main_workflow(self.wf_uuid)
        if wf is None:
            print "Workflow is not in main DB"
        else:
            # Delete the workflow (this will delete the main_workflowstate entries as well)
            mdb.delete_main_workflow(self.wf_uuid)

        # Update the main db
        mdbsession.commit()
        mdbsession.close()

class ExtractCommand(LoggingCommand):
    description = "Extract (uncompress) submit directory"
    usage = "Usage: %prog extract SUBMITDIR"

    def run(self):
        if len(self.args) != 1:
            self.parser.error("Specify SUBMITDIR")

        SubmitDir(self.args[0]).extract()

class ArchiveCommand(LoggingCommand):
    description = "Archive (compress) submit directory"
    usage = "Usage: %prog archive SUBMITDIR"

    def run(self):
        if len(self.args) != 1:
            self.parser.error("Specify SUBMITDIR")

        SubmitDir(self.args[0]).archive()

class MoveCommand(LoggingCommand):
    description = "Move a submit directory"
    usage = "Usage: %prog move SUBMITDIR DEST"

    def run(self):
        if len(self.args) != 2:
            self.parser.error("Specify SUBMITDIR and DEST")

        SubmitDir(self.args[0]).move(self.args[1])

class DeleteCommand(LoggingCommand):
    description = "Delete a submit directory and the associated DB entries"
    usage = "Usage: %prog delete SUBMITDIR"

    def run(self):
        if len(self.args) != 1:
            self.parser.error("Specify SUBMITDIR")

        SubmitDir(self.args[0]).delete()

class AttachCommand(LoggingCommand):
    description = "Attach a submit dir to the main db (dashboard)"
    usage = "Usage: %prog attach SUBMITDIR"

    def run(self):
        if len(self.args) != 1:
            self.parser.error("Specify SUBMITDIR")

        SubmitDir(self.args[0]).attach()

class DetachCommand(LoggingCommand):
    description = "Detach a submit dir from the main db (dashboard)"
    usage = "Usage: %prog detach SUBMITDIR"

    def run(self):
        if len(self.args) != 1:
            self.parser.error("Specify SUBMITDIR")

        SubmitDir(self.args[0]).detach()

class SubmitDirCommand(CompoundCommand):
    description = "Manages submit directories"
    commands = [
        ("archive", ArchiveCommand),
        ("extract", ExtractCommand),
        ("move", MoveCommand),
        ("delete", DeleteCommand),
        ("attach", AttachCommand),
        ("detach", DetachCommand)
    ]
    aliases = {
        "ar": "archive",
        "ex": "extract",
        "mv": "move",
        "rm": "delete",
        "at": "attach",
        "dt": "detach"
    }

def main():
    "The entry point for pegasus-submitdir"
    SubmitDirCommand().main()

