# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:16:30 2022

@author: aakaa
"""
###########################Import Required Libraries#############################
import face_recognition
#import dlib
import cv2
import numpy as np
import pandas as pd
import os
import threading
#################################################################################
os.chdir(r'/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/')
df=pd.read_csv('Data.csv')
cap=cv2.VideoCapture(0)
##############################Convert the encoding values already stored to a list###
encodeList=[]
for idx,encoding in enumerate(df['Encodings']):
    encoding=encoding.split(',')
    encoding=np.array(encoding)
    encoding=encoding.astype(float)
    encodeList.append(encoding)

print(encodeList)
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

def getDetails(encodings):
    name=input("Enter your name: ")
    s=np.sum(encodings)
    e=','.join(map(str,encodings))
    df.loc[len(df.index)]=[name,e,s]
    print("Sucessfully added data")
    encodeList.append(encodings)
###############################Main Driver Code###################################
if __name__=='__main__':
    while True:
        ret,frame=cap.read()
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faces=face_recognition.face_locations(img)
        encodeImg=face_recognition.face_encodings(img,faces)
        for eF,fL in zip(encodeImg,faces):
            name=findFace(eF)
            if name=='Un-identified Face':
                t=threading.Thread(target=getDetails,args=(eF,))
                t.start()
                t.join()
            cv2.putText(frame,name,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        cv2.imshow('Face Recog',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    df.to_csv('Data.csv',index=False)
###################################################################################