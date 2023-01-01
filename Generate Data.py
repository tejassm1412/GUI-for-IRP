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
# encodeImg=face_recognition.face_encodings(img)
# test_df=pd.DataFrame(index=[i for i in range(5)],columns=['Name','Encodings','SoE'])
# sumEncodings=np.sum(encodeImg)
# test_df.at[0,'Name']='Larry Page'
# test_df.at[0,'Encodings']=encodeImg[0]
# test_df.at[0,'SoE']=sumEncodings
# test_df.to_csv('Test.csv')
###################################################################################

''' Now we can iterate through the images in the celebrity folder and generate encoding values
for them and save them in the the CSV file for later use '''

##################################Main Code########################################
for idx,img in enumerate(imgs):
    imgPath=imgDir+f'/{img}'
    i=face_recognition.load_image_file(imgPath)
    i=cv2.cvtColor(i,cv2.COLOR_BGR2RGB)
    encodeImg=face_recognition.face_encodings(i)
    sumEncodings=np.sum(encodeImg)
    name=img.split('.')
    df.at[idx,'Name']=f'{name[0]}'
    df.at[idx,'Encodings']=','.join(map(str,encodeImg[0]))
    df.at[idx,'SoE']=sumEncodings
    
df.to_csv('Data.csv')

