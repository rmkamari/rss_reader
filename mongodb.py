from pymongo import MongoClient


def get_rss():
    try:
        client = MongoClient("mongodb://rssMd:rssMd1081qaz@"
                             "mongo-rs-0-mongod.percona-server-mongodb.autoip.dcos.thisdcos.directory,"
                             "mongo-rs-1-mongod.percona-server-mongodb.autoip.dcos.thisdcos.directory,"
                             "mongo-rs-2-mongod.percona-server-mongodb.autoip.dcos.thisdcos.directory:27017"
                             "/rssDb?replicaSet=rs")

        db = client.rssDb  # Connection to the database
        my_col = db['rss_link']
        return my_col.find({})
    except Exception as err:
        print(err)
        print("\nMongoDB  connection error!")

