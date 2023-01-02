import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import os
import PIL.Image, PIL.ImageTk
import cv2
from simple_facerec import SimpleFacerec
import dlib
import os
import pandas as pd
import numpy as np
import face_recognition
import speech_recognition as sr
from fpdf import FPDF
import pytesseract
import csv
import sys
import pyrealsense2 as rs
import numpy as np

PATH = os.path.dirname(os.path.realpath(__file__))
df=pd.read_csv(PATH + '/Data (copy).csv')
encodeList=[]
names=df['Name']
phone=df['Phone']
email=df['Email']
org=df['Organisation']
pov=df['Purpose']

class App():
    def __init__(self):
        self.face_recog()


    
    def face_recog(self):


        #os.chdir(r'/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/Celebrity Images')
        self.df=pd.read_csv(PATH + '/Data (copy).csv')
    
        ##############################Convert the encoding values already stored to a list###
        self.encodeList=[]
        for self.idx,encoding in enumerate(self.df['Encodings']):
            encoding=encoding.split(',')
            encoding=np.array(encoding)
            encoding=encoding.astype(float)
            self.encodeList.append(encoding)

        img = face_recognition.load_image_file("target.jpg")

        faces=face_recognition.face_locations(img)
        encodeImg=face_recognition.face_encodings(img,faces)
        for eF,fL in zip(encodeImg,faces):
            name=self.findFace(eF)
            if name == 'Un-identified Face' or name == 'Name Unavailable':
                print(name)

            elif name == self.list:
                self.input_name = self.names[self.idx]
                print(name[0])

    def findFace(self, encodeVal):
        dist=face_recognition.face_distance(self.encodeList,encodeVal)
        self.names=self.df['Name']
        self.phone=self.df['Phone']
        self.email=self.df['Email']
        self.org=self.df['Organisation']
        self.pov=self.df['Purpose']
        
        self.idx=np.argmin(dist)
        if dist[self.idx]>0.5:
            return 'Un-identified Face'
        else:
            if self.names[self.idx]:
                self.list = [self.names[self.idx], self.phone[self.idx], self.email[self.idx], self.org[self.idx], self.pov[self.idx], self.idx]
                return self.list
            else:
                return 'Name Unavailable'

    
App()
