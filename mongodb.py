from pymongo import MongoClient


def get_rss():
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client.rss_reader  # Connection to the database
        my_col = db['rss_link']
    except Exception as err:
        print(err + "\nMongoDB  connection error!")
    return my_col.find({})
