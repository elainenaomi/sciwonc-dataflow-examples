//drop database
//use config
//db.collections.remove( { _id: /^DATABASE\./ } )
//db.databases.remove( { _id: "DATABASE" } )
//db.chunks.remove( { ns: /^DATABASE\./ } )
//db.locks.remove( { _id: /^DATABASE\./ } )

//use config
// 1. stop the balancer
//db.settings.update({_id: "balancer"}, {$set: {stopped: true}}, true)
// 2. wait for in-progress migrations to finish, this may take a few seconds
//while (db.locks.findOne({_id: "balancer", state: {$ne: 0}}) != null) { sleep(1000); }
// 3. now you can safely drop the database
// use <dbname>
//switched to db <dbname>
// db.dropDatabase()
// enable the balancer
// db.settings.update({_id: "balancer"}, {$set: {stopped: false}}, true)

// stop the balancer
use config
db.settings.update({_id: "balancer"}, {$set: {stopped: true}}, true)
// wait for in-progress migrations to finish, this may take a few seconds
while (db.locks.findOne({_id: "balancer", state: {$ne: 0}}) != null) { sleep(1000); }

use google
db.ratio.remove({})
db.ratio.dropIndexes()
db.ratio.drop()
db.createCollection("ratio")
db.ratio.reIndex()

//drop collection
use config
db.collections.remove( { _id: "google.ratio" })
db.chunks.remove( { ns: "google.ratio" })
db.locks.remove( { _id: "google.ratio" })


//flush mongos
var mongoses = db.mongos.find()
while (mongoses.hasNext()) { new Mongo(mongoses.next()._id).getDB("admin").runCommand({flushRouterConfig: 1}) }

// enable the balancer
db.settings.update({_id: "balancer"}, {$set: {stopped: false}}, true)
