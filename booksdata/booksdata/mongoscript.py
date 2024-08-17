from pymongo import MongoClient
import datetime



client = MongoClient("mongodb+srv://awaz:9813510096%40Nj@awaz.8back.mongodb.net/")
db = client.scrappy
posts=db.test_collections




post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}


post_id = posts.insert_one(post).inserted_id