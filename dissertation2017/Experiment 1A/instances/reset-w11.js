use config;
db.settings.update({_id: "balancer"}, {$set: {stopped: true}}, true);
while (db.locks.findOne({_id: "balancer", state: {$ne: 0}}) != null) { sleep(1000); };


use googleh;
db.ratio.remove({});
db.ratio.dropIndexes();
db.ratio.drop();


//drop collection
use config;
db.collections.remove( { _id: "googleh.ratio" });
db.chunks.remove( { ns: "googleh.ratio" });
db.locks.remove( { _id: "googleh.ratio" });
db.settings.update({_id: "balancer"}, {$set: {stopped: false}}, true);

use googleh;
db.createCollection("ratio");
db.ratio.reIndex();
