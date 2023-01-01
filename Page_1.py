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

PATH = os.path.dirname(os.path.realpath(__file__))

"""
main_screen: Starting Screen
main_screen_1: Camera to capture person's image
main_screen_2: Recognise Person
main_screen_3: Unrecognised Options
main_screen_4: 

"""





class App(tkinter.Tk):


    def __init__(self):
        super().__init__()
        self.init_attributes()
        

    def init_attributes(self):
        self.title("Maya Gui")

        self.attributes('-zoomed', True)
        self.trigger = 3
        self.trig2 = 0 #Used o stop the update loop
        self.main_screen()
        self.i = 0
        self.y1 = ""
        self.y2 = ""
        self.y3 = ""
        self.y4 = ""

    def main_screen(self): #Start Screen

        self.config(bg = "#FFFFFF")

        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, bg = "#FFFFFF")
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, fg_color=None, bg = "#FFFFFF")
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500,100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image, bg = "#FFFFFF")
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #Poster+Instructions

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(1, weight= 1)

        #Poster

        self.poster_main_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20, bg = "#FFFFFF")
        self.poster_main_frame.grid(row=1, column = 1, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.poster_frame = tkinter.Frame(master=self.poster_main_frame, padx = 20, pady = 20, bg = "#FFFFFF")
        self.poster_frame.grid(row=0, column = 0, sticky = "nws")
        
        self.poster_frame.grid_columnconfigure(0, weight=1)
        self.poster_frame.grid_rowconfigure(0, weight=1)

        self.image2 = Image.open(PATH + "/bg_gradient.png")
        self.image_copy2 = self.image2.copy()
        self.poster_image = ImageTk.PhotoImage(self.image2)

        self.poster_label = tkinter.Label(master = self.poster_frame, image = self.poster_image, bg = "#FFFFFF")
        self.poster_label.grid(row = 0, column=0, sticky = "nwse")
        self.poster_label.bind('<Configure>', self.resizeImage)


        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20, bg = "#FFFFFF")
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Lets Go!",
                                                command=self.button_event_1, bg = "#0096FF")
        self.button.grid(row=1, column=0, sticky= "swe")

    def main_screen_1(self): #Capture Picture of the user



        self.video_source = 0

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture2(self.video_source)





        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, bg = "#FFFFFF")
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, bg = "#FFFFFF")
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image, bg = "#FFFFFF")
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #PosterConfig GRID

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(1, weight= 1)



        #Poster

        self.poster_main_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20, bg = "#F5F5F5")
        self.poster_main_frame.grid(row=1, column = 1, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.poster_frame = tkinter.Frame(master=self.poster_main_frame, padx = 20, pady = 20, bg = "#FFFFFF")
        self.poster_frame.grid(row=0, column = 0, sticky = "nws")
        
        self.poster_frame.grid_columnconfigure(0, weight=1)
        self.poster_frame.grid_rowconfigure(0, weight=1)

        self.poster_label = tkinter.Label(master = self.poster_frame, bg = "#FFFFFF")
        self.poster_label.grid(row = 0, column=0, sticky = "nwse")
        self.poster_label.bind('<Configure>', self.resizeImage)

        #Frame for main buttons such as Visiting Card and Manually
        self.capture_btn_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20, bg = "#FFFFFF")
        self.capture_btn_frame.grid(row = 2, column = 1, sticky = "sew")

        self.capture_btn_frame.grid_rowconfigure(0, weight=1)
        self.capture_btn_frame.grid_columnconfigure(0, weight= 1)

        self.captureButton = tkinter.Button(master=self.capture_btn_frame,
                                                text="Click",
                                                command=self.button_event_2,
                                                padx = 100, pady = 20)
        self.captureButton.grid(row = 0, column = 0, sticky = "sew")



        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, padx = 20, pady = 20, bg = "#F5F5F5")
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20, bg = "#FFFFFF")
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Back",
                                                command=self.button_event_2,bg = "#FFFFFF")
        self.button.grid(row=1, column=0, sticky= "nswe")


        # After it is called once, the update2 method will be automatically called every delay milliseconds
        self.delay = 15
        self.update2()

        self.mainloop()
        
        


    def main_screen_2(self): #Recognise Visitor

        
        #################################################################################
        
        self.video_source = 0
        self.vid = MyVideoCapture(self.video_source)
        
        
        #################################################################################
        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20)
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, fg_color=None)
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image)
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #PosterConfig GRID

        self.main_frame.grid_rowconfigure(1, weight=1)
        
        self.main_frame.grid_columnconfigure(0, weight=2)

        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Back",
                                                command=self.button_event_1,
                                                height=3)
        self.button.grid(row=1, column=0, sticky= "nswe")

        #Poster

        self.poster_main_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=0, column = 0, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.recog_label = tkinter.Label(master = self.poster_main_frame)
        self.recog_label.grid(row = 0, column = 0, sticky = "news")


        self.delay = 15
        self.update()

        self.mainloop()

    def main_screen_3(self): #Incase Unrecognised user, provide options to user for Manual and Visiting card based registration

        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20)
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, fg_color=None)
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image)
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #PosterConfig GRID

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(1, weight= 1)



        #Poster

        self.poster_main_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=1, column = 1, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.poster_frame = tkinter.Frame(master=self.poster_main_frame, padx = 20, pady = 20)
        self.poster_frame.grid(row=0, column = 0, sticky = "nws")
        
        self.poster_frame.grid_columnconfigure(0, weight=1)
        self.poster_frame.grid_rowconfigure(0, weight=1)

        self.image2 = Image.open(PATH + "/bg_gradient.png")
        self.image_copy2 = self.image2.copy()
        self.poster_image = ImageTk.PhotoImage(self.image2)

        self.poster_label = tkinter.Label(master = self.poster_frame, image = self.poster_image)
        self.poster_label.grid(row = 0, column=0, sticky = "nwse")
        self.poster_label.bind('<Configure>', self.resizeImage)


        #Frame for main buttons such as Visiting Card and Manually
        self.capture_btn_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20)
        self.capture_btn_frame.grid(row = 2, column = 1, sticky = "sew")

        self.capture_btn_frame.grid_rowconfigure(0, weight=1)
        self.capture_btn_frame.grid_columnconfigure(0, weight= 1)

        self.visitingCardButton = tkinter.Button(master=self.capture_btn_frame,
                                                text="Visiting Card",
                                                command=self.button_event_4,
                                                padx = 100, pady = 20)
        self.visitingCardButton.grid(row = 0, column = 0, sticky = "sew")

        self.ManualButton = tkinter.Button(master=self.capture_btn_frame,
                                                text="Manual",
                                                command=self.button_event_3, padx = 100, pady = 20)
        self.ManualButton.grid(row = 0, column = 1, sticky = "sew")

        self.capture_btn_frame.grid_rowconfigure(0, weight=1)
        self.capture_btn_frame.grid_columnconfigure(1, weight= 1)

        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Back",
                                                command=self.button_event_1)
        self.button.grid(row=1, column=0, sticky= "nswe")

    def main_screen_4(self): #Capture Picture of the user



        self.video_source = 0

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture3(self.video_source)
        
        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20)
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20)
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image)
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #PosterConfig GRID

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(1, weight= 1)



        #Poster

        self.poster_main_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=1, column = 1, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.poster_frame = tkinter.Frame(master=self.poster_main_frame, padx = 20, pady = 20)
        self.poster_frame.grid(row=0, column = 0, sticky = "nws")
        
        self.poster_frame.grid_columnconfigure(0, weight=1)
        self.poster_frame.grid_rowconfigure(0, weight=1)

        self.poster_label = tkinter.Label(master = self.poster_frame)
        self.poster_label.grid(row = 0, column=0, sticky = "nwse")

        #Frame for main buttons such as Visiting Card and Manually
        self.capture_btn_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20)
        self.capture_btn_frame.grid(row = 2, column = 1, sticky = "sew")

        self.capture_btn_frame.grid_rowconfigure(0, weight=1)
        self.capture_btn_frame.grid_columnconfigure(0, weight= 1)

        self.captureButton = tkinter.Button(master=self.capture_btn_frame,
                                                text="Click", command = self.button_event_7,
                                                width=50, padx = 100, pady = 20)
        self.captureButton.grid(row = 0, column = 0, sticky = "sew")



        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Back")
        self.button.grid(row=1, column=0, sticky= "nswe")


        # After it is called once, the update2 method will be automatically called every delay milliseconds
        self.delay = 15
        print("It should reach here")
        """
        self.update3()

        self.mainloop()

        """


    def main_screen_5(self): #Registration

        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20)
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, fg_color=None)
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image)
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #PosterConfig GRID

        self.main_frame.grid_rowconfigure(1, weight=1)
        
        self.main_frame.grid_columnconfigure(0, weight=2)


        #Registration Poster
        self.reg_frame = tkinter.Frame(master=self.main_frame, width=180, padx = 20, pady = 20)
        self.reg_frame.grid(row=0, column = 0, sticky = "news")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.reg_label = tkinter.Label(master = self.reg_frame, text = "Registration")
        self.reg_label.grid(row = 0, column = 0, sticky = "new")
        self.reg_label.configure(anchor = "center")
        self.reg_frame.grid_columnconfigure(0, weight=1)
        self.reg_frame.grid_rowconfigure(0, weight=1)
        self.reg_frame.grid_rowconfigure(1, weight=4)

        self.det_frame = tkinter.Frame(master=self.reg_frame, width=180, padx = 20, pady = 20)
        self.det_frame.grid(row=1, column = 0, sticky = "news")
        self.det_frame.grid_columnconfigure(0, weight=1)
        self.det_frame.grid_columnconfigure(1, weight=1)
        

        self.name_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20)
        self.email_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20)
        self.phone_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20)
        self.org_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20)
        self.pov_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20)

        self.name_frame.grid(row = 0, column = 0)
        self.email_frame.grid(row = 1, column = 0)
        self.phone_frame.grid(row = 2, column = 0)
        self.org_frame.grid(row = 3, column = 0)
        self.pov_frame.grid(row = 4, column = 0)

        self.name_label = tkinter.Label(master = self.name_frame, text = "Name")
        self.email_label = tkinter.Label(master = self.email_frame, text = "Email")
        self.phone_label = tkinter.Label(master = self.phone_frame, text = "Phone")
        self.org_label = tkinter.Label(master = self.org_frame, text = "Organisation")
        self.pov_label = tkinter.Label(master = self.pov_frame, text = "Purpose of Visit")

        self.name_label.grid(row = 0, column = 0)
        self.email_label.grid(row = 0, column = 0)
        self.phone_label.grid(row = 0, column = 0)
        self.org_label.grid(row = 0, column = 0)
        self.pov_label.grid(row = 0, column = 0)

        self.name_frame2 = tkinter.Frame(master=self.det_frame, width=180, padx = 40, pady = 40)
        self.email_frame2 = tkinter.Frame(master=self.det_frame, width=180, padx = 40, pady = 40)
        self.phone_frame2 = tkinter.Frame(master=self.det_frame, width=180, padx = 40, pady = 40)
        self.org_frame2 = tkinter.Frame(master=self.det_frame, width=180, padx = 40, pady = 40)
        self.pov_frame2 = tkinter.Frame(master=self.det_frame, width=180, padx = 40, pady = 40)

        self.name_frame2.grid(row = 0, column = 1)
        self.email_frame2.grid(row = 1, column = 1)
        self.phone_frame2.grid(row = 2, column = 1)
        self.org_frame2.grid(row = 3, column = 1)
        self.pov_frame2.grid(row = 4, column = 1)

        self.name_text = tkinter.Text(master = self.name_frame2, height = 2)
        self.email_text = tkinter.Text(master = self.email_frame2, height = 2)
        self.phone_text = tkinter.Text(master = self.phone_frame2, height = 2)
        self.org_text = tkinter.Text(master = self.org_frame2, height = 2)
        self.pov_text = tkinter.Text(master = self.pov_frame2, height = 2)


        self.name_text.grid(row = 0, column = 0)
        self.email_text.grid(row = 0, column = 0)
        self.phone_text.grid(row = 0, column = 0)
        self.org_text.grid(row = 0, column = 0)
        self.pov_text.grid(row = 0, column = 0)
        
        




        #Frame for S2T and Submit
        self.speak_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20)
        self.speak_frame.grid(row = 2, column = 0, sticky = "sewn")

        self.speak_frame.grid_rowconfigure(0, weight=1)
        self.speak_frame.grid_columnconfigure(0, weight= 1)

        self.speakButton = tkinter.Button(master=self.speak_frame,
                                                text="Speak Up!",
                                                command=self.button_event_5,
                                                height=2, padx = 100, pady = 20)
        self.speakButton.grid(row = 0, column = 0, sticky = "s")

        self.Submit_Button = tkinter.Button(master=self.speak_frame,
                                                text="Submit",
                                                command=self.button_event_x,
                                                height=2, padx = 100, pady = 20)
        self.Submit_Button.grid(row = 0, column = 1, sticky = "s")

        self.speak_frame.grid_rowconfigure(0, weight=1)
        self.speak_frame.grid_columnconfigure(1, weight= 1)

        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Back")
        self.button.grid(row=1, column=0, sticky= "nswe")

        self.idx = self.list[5]


        if self.param1 == "alert":
            if self.trigger == 0:
                print("YupYupYup")
                self.name_text.insert(tkinter.END, self.list2[0])
                self.email_text.insert(tkinter.END, self.list2[1])
                self.phone_text.insert(tkinter.END, self.list2[2])
                self.org_text.insert(tkinter.END, self.list2[3])



            else:
                
                
                self.name_text.insert(tkinter.END, self.list[0])
                self.email_text.insert(tkinter.END, self.list[2])
                self.phone_text.insert(tkinter.END, self.list[1])
                self.org_text.insert(tkinter.END, self.list[3])

        else: 
            pass

    def main_screen_6(self): #Card Picture Capture Frame
        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, corner_radius=0, padx = 20, pady = 20)
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, corner_radius=0, padx = 20, pady = 20, fg_color=None)
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image)
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #PosterConfig GRID

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight= 1)



        #Poster

        self.poster_main_frame = tkinter.Frame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=0, column = 0, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.ocr_text_frame = tkinter.Frame(master=self.poster_main_frame, corner_radius=0, padx = 20, pady = 20)
        self.ocr_text_frame.grid(row=0, column = 0, sticky = "ns")
        
        self.ocr_text_frame.grid_columnconfigure(0, weight=1)
        self.ocr_text_frame.grid_rowconfigure(0, weight=1)

        self.ocr_text = tkinter.Text(master = self.ocr_text_frame, height=20, width=1000)
        self.ocr_text.grid(row = 0, column = 0, sticky = "ew")

        self.radio_frame = tkinter.Frame(master=self.poster_main_frame, corner_radius=0, padx = 20, pady = 20)
        self.radio_frame.grid(row=1, column = 0, sticky = "ns")

        self.radio_var = tkinter.IntVar()


        self.radio_button_1 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=0, text="Name")
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_2 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=1, text="Email")
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_3 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=2, text="Phone")
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_4 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=3, text="Organisation")
        self.radio_button_4.grid(row=4, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_5 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=4, text="Skip")
        self.radio_button_5.grid(row=5, column=0, pady=10, padx=20, sticky="nw")



        #Frame for main buttons such as Visiting Card and Manually
        self.buttons_frame = tkinter.Frame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.buttons_frame.grid(row = 1, column = 0, sticky = "sew")

        self.buttons_frame.grid_rowconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(0, weight= 1)

        self.submit_Button = tkinter.Button(master=self.buttons_frame,
                                                text="Next",
                                                command=self.button_event_8, padx = 100, pady = 20)
        self.submit_Button.grid(row = 0, column = 0, sticky = "sew")


        


        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, corner_radius=0, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, 
                                                    text= "Instructions\nChoose what field the info\nbelongs to.\n\nSkip in case:\nInfo is irrelevant\nInfo is Blank\n\n", 
                                                    padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Back",
                                                command=self.button_event,
                                                height=50, width=50)
        self.button.grid(row=1, column=0, sticky= "nswe")
        self.reset()
        self.ocr_recognise()
        

    def main_screen_7(self):

        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20)
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, fg_color=None)
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image)
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")


        #PosterConfig GRID

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight= 1)



        #Poster

        self.poster_main_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=0, column = 0, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.ocr_text_frame = tkinter.Frame(master=self.poster_main_frame, padx = 20, pady = 20)
        self.ocr_text_frame.grid(row=0, column = 0, sticky = "ns")
        
        self.ocr_text_frame.grid_columnconfigure(0, weight=1)
        self.ocr_text_frame.grid_rowconfigure(0, weight=1)

        self.ocr_text = tkinter.Text(master = self.ocr_text_frame, height=20, width=1000)
        self.ocr_text.grid(row = 0, column = 0, sticky = "ew")

        self.radio_frame = tkinter.Frame(master=self.poster_main_frame, padx = 20, pady = 20)
        self.radio_frame.grid(row=1, column = 0, sticky = "ns")

        self.radio_var = tkinter.IntVar()


        self.radio_button_1 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=0, text="Name")
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_2 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=1, text="Email")
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_3 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=2, text="Phone")
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_4 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=3, text="Organisation")
        self.radio_button_4.grid(row=4, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_5 = tkinter.Radiobutton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=4, text="Skip")
        self.radio_button_5.grid(row=5, column=0, pady=10, padx=20, sticky="nw")



        #Frame for main buttons such as Visiting Card and Manually
        self.buttons_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20)
        self.buttons_frame.grid(row = 1, column = 0, sticky = "sew")

        self.buttons_frame.grid_rowconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(0, weight= 1)

        self.submit_Button = tkinter.Button(master=self.buttons_frame,
                                                text="Next",
                                                command=self.button_event_8,padx = 100, pady = 20)
        self.submit_Button.grid(row = 0, column = 0, sticky = "sew")


        


        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, 
                                                    text= "Instructions\nChoose what field the info\nbelongs to.\n\nSkip in case:\nInfo is irrelevant\nInfo is Blank\n\n", 
                                                    padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Back")
        self.button.grid(row=1, column=0, sticky= "nswe")
        self.reset()
        self.ocr_recognise()




    def button_event_1(self):#Camera Frame Activate

        y = self.msg_box()
        if y=="yes":
            
            self.destroy_window()
            self.main_screen_1()
        else:
            print("No")

    def button_event_2(self):#Capture Person Image and activate face recog
        
        self.snapshot()
        y = self.msg_box()
        if y=="yes":
            self.vid.released()
            cv2.destroyAllWindows()
            self.destroy_window()
            self.main_screen_2()
        else:
            print("No")

    def button_event_3(self):#Manual process

        self.trigger = 1 #used later for differentiating the the final pages for these options
        print("trigger = 1")
        y = self.msg_box()
        if y=="yes":
            self.destroy_window()
            self.main_screen_5()
        else:
            print("No")

    def button_event_4(self): #Leads to Visitor setup
        y = self.msg_box()
        if y=="yes":
            print("I was Here")
            self.vid.released()
            cv2.destroyAllWindows()
            self.destroy_window()
            self.main_screen_4() #LOL
        else:
            print("No")

    def button_event_5(self): #Speech to text input Value in the boxes
        # name email phone org pov
        
        
        self.text_declaration()
        y=self.speechToTextFn()
        print("Y = "+y)
        if self.x1 == "":
            self.name_text.insert(tkinter.END, y)
            self.x1 = y


        elif self.x2 == "":
            y = y.split(" ")
            y = "".join(y)
            y = y.lower()
            y = y.split("attherate")
            y = "@".join(y)
            y = y.split("dot")
            y = ".".join(y)
            self.email_text.insert(tkinter.END, y)
            self.x2 = y

        elif self.x3 == "":
            y = y.split(" ")
            y = "".join(y)
            self.phone_text.insert(tkinter.END, y)
            self.x3 = y

        elif self.x4 == "":
            self.org_text.insert(tkinter.END, y)
            self.x4 = y

        elif self.x5 == "":
            self.pov_text.insert(tkinter.END, y)
            self.x5 = y

        else:
            pass

    def button_event_6(self): #Open Visiting Card OCR Frame
        y = self.msg_box()
        if y=="yes":

            print("I was Here")
            self.vid.released()
            cv2.destroyAllWindows()
            self.destroy_window()
            self.main_screen_7()
        else:
            print("No")

    def button_event_7(self):#Capture Card Image and activate face recog
        
        self.snapshot2()
        y = self.msg_box()
        if y=="yes":
            self.vid.released()
            cv2.destroyAllWindows()
            self.destroy_window()
            self.main_screen_7()
        else:
            print("No")

    def button_event_8(self):
        self.data_match()
        self.destroy_window()
        self.main_screen_7()
        self.ocr_text.insert(tkinter.END, self.ocrs[self.i])
        
        self.i += 1
        print(self.i)
        print(len(self.ocrs))
        

        if self.i >= len(self.ocrs):
            self.ocr_text.insert(tkinter.END, "Done")
            self.i = 0
            print("Strings Are:", self.y1, self.y2, self.y3, self.y4)
            print("y1 =", self.y1, "\n", "y2 =", self.y2, "\n", "y3 =", self.y3, "\n", "y4 =", self.y4, "\n", )
            self.list2 = [self.y1, self.y2, self.y3, self.y4] #Name, Email, Phone, Organisation, in that order
            self.trigger = 0
            self.destroy_window()
            self.main_screen_5()

    def button_event_x(self): #Final Submit
        y = self.msg_box()
        if y == "yes":
            if self.param2 == "Un-identified Face":
                self.text_declaration()
                self.pdf_create()
                self.encoding_store()
                self.destroy()
                sys.exit()


            else:
                self.text_declaration()
                self.pdf_create()
                self.update_data()
                self.destroy()
                sys.exit()

        
        else:
            print("No")

    def snapshot(self): #For Visitor Pic
        # Get a frame from the video source
        self.ret, frame = self.vid.get_frame()

        if self.ret:
            cv2.imwrite(PATH+"/target.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))   

    

    def snapshot2(self): #For visiting card
        # Get a frame from the video source
        self.ret, frame = self.vid.get_frame()

        if self.ret:
            cv2.imwrite(PATH+"/target2.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update2(self):
        # Get a frame from the video source
        self.ret, frame = self.vid.get_frame()

        if self.ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.poster_label.config(image = self.photo)

        self.after(self.delay, self.update2)

    def update3(self):
        # Get a frame from the video source
        self.ret, frame = self.vid.get_frame()

        if self.ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.poster_label.config(image = self.photo)

        self.after(self.delay, self.update2)



    def update(self): 
        # Get a frame from the video source
        self.ret, self.frame = self.vid.get_frame()
        
        if self.ret:
            self.param1 = self.ret
            self.param2 = self.frame
            if self.ret == "alert": #Alert found Face
                
                if self.frame == 'Un-identified Face':
                    
                    self.list = ["", "", "", "", "", ""]
                    self.destroy_window()
                    self.vid.released()
                    cv2.destroyAllWindows()
                    
                    self.trig2 = 1
                    self.main_screen_3()
                else:
                    self.list = self.frame
                    self.destroy_window()
                    self.vid.released()
                    self.trig2 = 1
                    cv2.destroyAllWindows()
                    self.main_screen_5()


            else: 
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
                self.recog_label.config(image = self.photo)


            print("I Entered Here")
            self.after(self.delay, self.update)

        if self.trig2 == 1:
            self.vid.released()
            cv2.destroyAllWindows()



    def destroy_window(self):
        for widgets in self.winfo_children():
            widgets.destroy()


    def speechToTextFn(self):


        # Set up the speech recognition
        r = sr.Recognizer()
        mic = sr.Microphone()
        # Start listening for speech
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            # Attempt to transcribe the speech
            transcription = r.recognize_google(audio)
            # Update the transcription label
            return transcription
        except Exception as e:
            # If there is an error, print it to the console
            print(e)

    
    


    
    def text_declaration(self):
        self.x1=self.name_text.get("1.0", "end-1c")
        self.x2=self.email_text.get("1.0", "end-1c")
        self.x3=self.phone_text.get("1.0", "end-1c")
        self.x4=self.org_text.get("1.0", "end-1c")
        self.x5=self.pov_text.get("1.0", "end-1c")



    def pdf_create(self):
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 10)
        
        data={'name': self.x1,'Email Address':self.x2, 'Mobile Number': self.x3, 'Organization': self.x4, 'POV': self.x5}
        
        pdf.cell(200,10,f"Name:  {data['name']}",ln=1,align='L')
        pdf.cell(200,10,f"Email: {data['Email Address']}",ln=2,align='L')
        pdf.cell(200,10,f"Mobile No.: {data['Mobile Number']}",ln=3,align='L')
        pdf.cell(200,10,f"Organization: {data['Organization']}",ln=4,align='L')
        pdf.cell(200,10,f"Purpose of Visit: {data['POV']}",ln=5,align='L')
        pdf.image(f'/home/tejas/Desktop/MySTuff/20-11-2022/target.jpg',x=10,y=60,w=60,h=70)
        pdf.output(f"/home/tejas/Desktop/MySTuff/20-11-2022/PDFs/{data['name']}_LTTS_Pass.pdf")




    def msg_box(self):
        x=tkinter.messagebox.askquestion("Confirmation", "Are you Sure")
        return x

    def destroy_window(self):
        for widgets in self.winfo_children():
            widgets.destroy()

    def resizeImage(self, event):
        image = self.image_copy2.resize(
            (self.poster_frame.winfo_width(), self.poster_frame.winfo_height()))
        self.newimage = ImageTk.PhotoImage(image)
        #print(self.poster_frame.winfo_width(), self.poster_frame.winfo_height())
        self.poster_label.configure(image = self.newimage)


    def reset(self):
        self.x1 = ""
        self.x2 = ""
        self.x3 = ""
        self.x4 = ""
        self.x5 = ""

    

    def ocr_recognise(self):
        self.img = cv2.imread(PATH+'/target2.jpg')

        self.img = cv2.resize(self.img, (600, 360))
        #print(pytesseract.image_to_string(self.img))
        self.a = pytesseract.image_to_string(self.img)
        self.b = self.a.split("\n")
        self.ocrs = []
        for a in self.b:
            if a != '' and a!= "\x0c":
                self.ocrs.append(a)

        print(self.ocrs)

    def destroy_window(self):
        for widgets in self.winfo_children():
            widgets.destroy()



        

    

    def data_match(self):
        self.rv = self.get_radio()
        self.boxVal = self.ocr_text.get("1.0", "end-1c")
        print("RadioVal = ",self.rv)

        if self.rv == "0":
            if self.y1 == "":
                self.x1 = self.boxVal
                self.y1 = self.x1
            else:
                self.x1 = self.y1 + " " + self.boxVal
                self.y1 = self.x1

        if self.rv == "1":
            if self.y2 == "":
                self.x2 = self.boxVal
                self.y2 = self.x2
            else:
                self.x2 = self.y2 + " " + self.boxVal
                self.y2 = self.x2

        if self.rv == "2":
            if self.y3 == "":
                self.x3 = self.boxVal
                self.y3 = self.x3
            else:
                self.x3 = self.y3 + " / " + self.boxVal
                self.y3 = self.x3

        if self.rv == "3":
            if self.y2 == "":
                self.x4 = self.boxVal
                self.y4 = self.x4
            else:
                self.x4 = self.y4 + " " + self.boxVal
                self.y4 = self.x4

        if self.rv == "4":
            pass

    def get_radio(self):
        self.radioVal = str(self.radio_var.get())
        return self.radioVal

    
        
    def update_data(self):
        # reading the csv file
        self.df = pd.read_csv("/home/tejas/Desktop/MySTuff/20-11-2022/Data (copy).csv")
        print(self.x1, self.x2, self.x3, self.x4, self.x5, self.idx)

        # updating the column value/data
        self.df.loc[self.idx, 'Name'] = self.x1
        self.df.loc[self.idx, 'Email'] = self.x2
        self.df.loc[self.idx, 'Phone'] = self.x3
        self.df.loc[self.idx, 'Organisation'] = self.x4
        self.df.loc[self.idx, 'Purpose'] = self.x5

        # writing into the file
        self.df.to_csv("Data (copy).csv", index=False)

    
    def encoding_store(self):
        
        # Load the image and detect the faces
        image = cv2.imread(PATH+'/target.jpg')
        face_locations = face_recognition.face_locations(image)

        # Extract the face encoding values for each face
        encodings = face_recognition.face_encodings(image, face_locations)

        # Open the CSV file in append mode
        with open('/home/tejas/Desktop/MySTuff/20-11-2022/Data (copy).csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the titles on the first row
            if csvfile.tell()==0:
                writer.writerow(['', 'Name', 'Encodings', "SoE", "Email","Phone","Organisation","Purpose"])
            for i, encoding in enumerate(encodings):
                #x = len(self.df.index)
                # Convert the encoding to a string separated by ","
                encoding_str = ",".join(str(x) for x in encoding)
                writer.writerow([i, self.x1, encoding_str, '', self.x2, self.x3, self.x4, self.x5])







    def resizeImage(self, event):
        image = self.image_copy2.resize(
            (self.poster_frame.winfo_width(), self.poster_frame.winfo_height()))
        self.newimage = ImageTk.PhotoImage(image)
        #print(self.poster_frame.winfo_width(), self.poster_frame.winfo_height())
        self.poster_label.configure(image = self.newimage)




class MyVideoCapture: #For Face Recognition

    def __init__(self, video_source=0):
        # Open the video source
        os.chdir(r'/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/Celebrity Images')
        self.df=pd.read_csv('/home/tejas/Desktop/MySTuff/20-11-2022/Data (copy).csv')
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
            self.ret,frame=self.vid.read()
            img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            faces=face_recognition.face_locations(img)
            encodeImg=face_recognition.face_encodings(img,faces)
            for eF,fL in zip(encodeImg,faces):
                name=self.findFace(eF)
                if name == 'Un-identified Face' or name == 'Name Unavailable':
                    self.vid.release()
                    cv2.destroyAllWindows()
                    return "alert", name

                elif name == self.list:
                    self.input_name = self.names[self.idx]
                    self.vid.release()
                    cv2.destroyAllWindows()
                    return "alert", self.list
            if self.ret:
                return (self.ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

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
        self.phone=self.df['Phone']
        self.email=self.df['Email']
        self.org=self.df['Organisation']
        self.pov=self.df['Purpose']
        
        self.idx=np.argmin(dist)
        if dist[self.idx]>0.4:
            return 'Un-identified Face'
        else:
            if self.names[self.idx]:
                self.list = [self.names[self.idx], self.phone[self.idx], self.email[self.idx], self.org[self.idx], self.pov[self.idx], self.idx]
                return self.list
            else:
                return 'Name Unavailable'

    def destroy_window(self):
        for widgets in self.winfo_children():
            widgets.destroy()

    def released(self):
        self.vid.release()
        cv2.destroyAllWindows()


class MyVideoCapture2:#For Capturing Image of the user
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def rescale_frame(self, frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

    def get_frame(self):
        if self.vid.isOpened():
            self.ret, frame = self.vid.read()
            frame_2 = self.rescale_frame(frame, percent = 200)
            if self.ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (self.ret, cv2.cvtColor(frame_2, cv2.COLOR_BGR2RGB))
            else:
                return (self.ret, None)
        else:
            return (self.ret, None)

    def released(self):
        self.vid.release()
        cv2.destroyAllWindows()

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()



class MyVideoCapture3:#For Capturing Image of the visiting card
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def rescale_frame(self, frame, percent=75):
        width = int(frame.shape[1] * percent/ 100)
        height = int(frame.shape[0] * percent/ 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

    def get_frame(self):
        if self.vid.isOpened():
            self.ret, frame = self.vid.read()
            frame_2 = self.rescale_frame(frame, percent = 200)
            if self.ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (self.ret, cv2.cvtColor(frame_2, cv2.COLOR_BGR2RGB))
            else:
                return (self.ret, None)
        else:
            return (self.ret, None)

    def released(self):
        self.vid.release()
        cv2.destroyAllWindows()

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


    def update(self): 
        # Get a frame from the video source
        self.ret, self.frame = self.vid.get_frame()
        
        if self.ret:
            self.param1 = self.ret
            self.param2 = self.frame
            if self.ret == "alert": #Alert found Face
                
                if self.frame == 'Un-identified Face':
                    
                    self.list = ["", "", "", "", "", ""]
                    self.destroy_window()
                    self.vid.released()
                    cv2.destroyAllWindows()
                    
                    self.trig2 = 1
                    self.main_screen_3()
                else:
                    self.list = self.frame
                    self.destroy_window()
                    self.vid.released()
                    self.trig2 = 1
                    cv2.destroyAllWindows()
                    self.main_screen_5()


            else: 
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
                self.recog_label.config(image = self.photo)


            print("I Entered Here")
            self.after(self.delay, self.update)


if __name__ == "__main__":

    app = App()
    app.mainloop()
