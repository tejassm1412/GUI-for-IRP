from deepface import DeepFace
import os
from deepface.commons import functions
from tqdm import tqdm
import pandas as pd

from pymongo import MongoClient
connection = "mongodb+srv://irp:irp2022@irpmongodb.26cuy7l.mongodb.net/test"

client = MongoClient(connection)

database = 'deepface'
collection = 'deepface'

db = client[database]

model = DeepFace.build_model("Facenet")

facial_img_paths = []
for root, directory, files in os.walk("/home/tejas/Desktop/MySTuff/20-11-2022/Mongo/Celebrity Images"):
    for file in files:
        if '.jpg' in file:
            facial_img_paths.append(root+"/"+file)


instances = []
 
for i in tqdm(range(0, len(facial_img_paths))):
    facial_img_path = facial_img_paths[i]
    facial_img = functions.preprocess_face(facial_img_path, target_size = (160, 160), enforce_detection = False)
     
    embedding = model.predict(facial_img)[0]

    instance = []
    instance.append(facial_img_path)
    instance.append(embedding)
    instances.append(instance)


df = pd.DataFrame(instances, columns = ["img_name", "embedding"])
df.head()
def insert():
    for index, instance in tqdm(df.iterrows(), total = df.shape[0]):
        print(index, instance)
        db[collection].insert_one({"img_path": instance["img_name"], "embedding" : instance["embedding"].tolist()})
insert()
target_img_path = "/home/tejas/Desktop/MySTuff/20-11-2022/Mongo/target.jpg"
target_img = functions.preprocess_face(target_img_path, target_size = (160, 160))
target_embedding = model.predict(target_img)[0].tolist()


query = db[collection].aggregate( [
{
    "$addFields": { 
        "target_embedding": target_embedding
    }
}
, {"$unwind" : { "path" : "$embedding", "includeArrayIndex": "embedding_index"}}
, {"$unwind" : { "path" : "$target_embedding", "includeArrayIndex": "target_index" }}
, {
    "$project": {
        "img_path": 1,
        "embedding": 1,
        "target_embedding": 1,
        "compare": {
            "$cmp": ['$embedding_index', '$target_index']
        }
    }
}
, {
  "$group": {
    "_id": "$img_path",
    "distance": {
            "$sum": {
                "$pow": [{
                    "$subtract": ['$embedding', '$target_embedding']
                }, 2]
            }
    }
  }
}
, { 
    "$project": {
        "_id": 1
        #, "distance": 1
        , "distance": {"$sqrt": "$distance"}
    }
}
] )
for i in query:
    print(i)


