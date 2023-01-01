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
import customtkinter
import tkinter.messagebox
import customtkinter
import PIL.Image, PIL.ImageTk
from PIL import Image, ImageTk

import os


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))

class App(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.attributes('-zoomed', True)
        self.main_screen_1()

    def main_screen_1(self):

        
        #################################################################################
        
        self.video_source = 0
        self.vid = MyVideoCapture(self.video_source)
        
        
        #################################################################################
        #main Container
        self.main_frame = customtkinter.CTkFrame(master=self, width=180, corner_radius=0, padx = 20, pady = 20)
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = customtkinter.CTkFrame(master=self, width=180, corner_radius=0, padx = 20, pady = 20, fg_color=None)
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((100, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = customtkinter.CTkLabel(master = self.logo_frame, image = self.logo_image)
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #PosterConfig GRID

        self.main_frame.grid_rowconfigure(1, weight=1)
        
        self.main_frame.grid_columnconfigure(0, weight=2)

        #Instructions

        self.instruction_frame = customtkinter.CTkFrame(master=self, corner_radius=0, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = customtkinter.CTkLabel(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = customtkinter.CTkButton(master=self.instruction_frame,
                                                text="Back",
                                                command=self.button_event,
                                                height=50, width=50)
        self.button.grid(row=1, column=0, sticky= "nswe")

        #Poster

        self.poster_main_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=0, column = 0, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.recog_label = customtkinter.CTkLabel(master = self.poster_main_frame)
        self.recog_label.grid(row = 0, column = 0, sticky = "news")


        self.delay = 15
        self.update()

        self.mainloop()







    def update(self):
        # Get a frame from the video source
        
        ret, frame = self.vid.get_frame()
        if ret:
            if ret == "alert":
                print(frame)
                self.destroy_window()

            elif ret: 
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
                self.recog_label.configure(image = self.photo)

        self.after(self.delay, self.update)
            

            
    
    def button_event():
        pass

    
    
        
                

        #self.cap.release()
        #cv2.destroyAllWindows()


    def destroy_window(self):
        for widgets in self.winfo_children():
            widgets.destroy()



class MyVideoCapture:

    def __init__(self, video_source=0):
        # Open the video source
        os.chdir(r'/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/Celebrity Images')
        self.df=pd.read_csv('/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/Data.csv')
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        ##############################Convert the encoding values already stored to a list###
        self.encodeList=[]
        for self.idx,encoding in enumerate(self.df['Encodings']):
            encoding=encoding.split(',')
            encoding=np.array(encoding)
            encoding=encoding.astype(float)
            self.encodeList.append(encoding)

    def rescale_frame(self, frame, percent=500):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

    def get_frame(self):
        if self.vid.isOpened():
            ret,frame=self.vid.read()
            img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            faces=face_recognition.face_locations(img)
            encodeImg=face_recognition.face_encodings(img,faces)
            for eF,fL in zip(encodeImg,faces):
                name=self.findFace(eF)
                cv2.putText(frame,name,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                if name == 'Un-identified Face' or name == 'Name Unavailable':
                    return "alert", name

                elif name == self.names[self.idx]:
                    self.input_name = self.names[self.idx]
                    self.vid.release()
                    cv2.destroyAllWindows()
                    return "alert", self.input_name
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        else:

            cv2.destroyAllWindows()
            return (None, None)
            #cv2.imshow('Face Recog',frame)

    
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    ######################################################################################
    def findFace(self, encodeVal):
        dist=face_recognition.face_distance(self.encodeList,encodeVal)
        self.names=self.df['Name']
        self.idx=np.argmin(dist)
        if dist[self.idx]>0.6:
            return 'Un-identified Face'
        else:
            if self.names[self.idx]:
                return self.names[self.idx]
            else:
                return 'Name Unavailable'

    def destroy_window(self):
        for widgets in self.winfo_children():
            widgets.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()

