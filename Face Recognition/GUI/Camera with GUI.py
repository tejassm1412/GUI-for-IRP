# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:34:30 2022

@author: aakaa
"""

from tkinter import *
from PIL import Image, ImageTk
import cv2
import face_recognition
from LiveCamera import findFace

win=Tk()
win.geometry("700x700")

label=Label(win)
label.grid(row=0,column=0)

cap=cv2.VideoCapture(0)

def showFrames():
    ret,img=cap.read()
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    faces=face_recognition.face_locations(img)
    encodeImg=face_recognition.face_encodings(img,faces)
    for eF,fL in zip(encodeImg,faces):
        name=findFace(eF)
        cv2.putText(img,name,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    image=Image.fromarray(img)
    imgTk=ImageTk.PhotoImage(image)
    label.imgtk=imgTk
    label.configure(image=imgTk)
    label.after(20,showFrames)
    
if __name__=='__main__':
    showFrames()
    win.mainloop()
    cap.release()