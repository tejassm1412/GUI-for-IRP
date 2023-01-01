# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:15:57 2022

@author: aakaa
"""

###########################Import Required Libraries#############################
import face_recognition
#import dlib
import cv2
import numpy as np
import pandas as pd
import os
#################################################################################
os.chdir(r'/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/Celebrity Images')
df=pd.read_csv('/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/Data.csv')
cap=cv2.VideoCapture(0)
##############################Convert the encoding values already stored to a list###
encodeList=[]
for idx,encoding in enumerate(df['Encodings']):
    encoding=encoding.split(',')
    encoding=np.array(encoding)
    encoding=encoding.astype(float)
    encodeList.append(encoding)
######################################################################################
def findFace(encodeVal):
    dist=face_recognition.face_distance(encodeList,encodeVal)
    names=df['Name']
    idx=np.argmin(dist)
    if dist[idx]>0.6:
        return 'Un-identified Face'
    else:
        if names[idx]:
            return names[idx]
        else:
            return 'Name Unavailable'
###############################Main Driver Code###################################
if __name__=='__main__':
    while True:
        ret,frame=cap.read()
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faces=face_recognition.face_locations(img)
        encodeImg=face_recognition.face_encodings(img,faces)
        for eF,fL in zip(encodeImg,faces):
            name=findFace(eF)
            cv2.putText(frame,name,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow('Face Recog',frame)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
###################################################################################