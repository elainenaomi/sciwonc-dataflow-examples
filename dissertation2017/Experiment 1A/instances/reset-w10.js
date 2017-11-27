use config;
db.settings.update({_id: "balancer"}, {$set: {stopped: true}}, true);
while (db.locks.findOne({_id: "balancer", state: {$ne: 0}}) != null) { sleep(1000); };


use googler;
db.ratio.remove({});
db.ratio.dropIndexes();
db.ratio.drop();


//drop collection
use config;
db.collections.remove( { _id: "googler.ratio" });
db.chunks.remove( { ns: "googler.ratio" });
db.locks.remove( { _id: "googler.ratio" });
db.settings.update({_id: "balancer"}, {$set: {stopped: false}}, true);

use googler;
db.createCollection("ratio");
db.ratio.reIndex();
