# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:29:59 2022

@author: aakaa
"""

###########################Import Required Libraries#############################
import face_recognition
import dlib
import cv2
import numpy as np
import pandas as pd
import os
#################################################################################

from pymongo import MongoClient
connection = "mongodb+srv://irp:irp2022@irpmongodb.26cuy7l.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection)

database = 'deepface'
collection = 'deepface'
db = client[database]

#########################Define Required Paths and variables#####################
imgDir='/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/Celebrity Images'
imgs=os.listdir(imgDir)
n=len(imgs)
df=pd.DataFrame(index=[i for i in range(n)],columns=['Name','Encodings','SoE'])
#################################################################################

'''Though before getting started with the images in the celebrity images folder,
first let us test on a image and see how to store the encoding values in a pandas dataframe'''
############################Test Img###############################################
# imgPath=r'D:\Environments\Humanoid\Face Recognition\Single Image Test\Larry Page.jpg'
# img=face_recognition.load_image_file(imgPath)
# img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# embedding=face_recognition.face_encodings(img)
# test_df=pd.DataFrame(index=[i for i in range(5)],columns=['Name','Encodings','SoE'])
# sumEncodings=np.sum(embedding)
# test_df.at[0,'Name']='Larry Page'
# test_df.at[0,'Encodings']=embedding[0]
# test_df.at[0,'SoE']=sumEncodings
# test_df.to_csv('Test.csv')
###################################################################################

''' Now we can iterate through the images in the celebrity folder and generate encoding values
for them and save them in the the CSV file for later use '''

##################################Main Code########################################

def insert():
    for idx,img in enumerate(imgs):
        print(idx, img)
        imgPath=imgDir+f'/{img}'
        i=face_recognition.load_image_file(imgPath)
        i=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
        embedding_encode=face_recognition.face_encodings(i)
        embedding = embedding_encode[0]
        sumEncodings=np.sum(embedding)
        name=img.split('.')
        #df.at[idx,'Name']=f'{name[0]}'
        #df.at[idx,'Encodings']=','.join(map(str,embedding[0]))
        #df.at[idx,'SoE']=sumEncodings
        db[collection].insert_one({"img_path": img, "embedding" :embedding.tolist(), "SoE": sumEncodings})
        #df.to_csv('Data.csv')



#insert()


target_img_path = "target.jpg"
i=face_recognition.load_image_file(target_img_path)
i=face_recognition.load_image_file(target_img_path)
i=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
embedding_encode=face_recognition.face_encodings(i)
target_embedding = embedding_encode[0]
db[collection].insert_one({"img_path": target_img_path, "embedding" :target_embedding.tolist()})




query = db[collection].aggregate( [
{
    "$addFields": { 
        "target_embedding": target_embedding.tolist()
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