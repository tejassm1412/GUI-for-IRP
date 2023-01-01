import tkinter
import tkinter.messagebox
import customtkinter
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

import threading

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


class App(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.title("Maya Gui")

        self.attributes('-zoomed', True)
        self.main_screen()

    def main_screen(self):


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


        #Poster+Instructions

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=2)

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(1, weight= 1)

        #Poster

        self.poster_main_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=1, column = 1, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.poster_frame = customtkinter.CTkFrame(master=self.poster_main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_frame.grid(row=0, column = 0, sticky = "nws")
        
        self.poster_frame.grid_columnconfigure(0, weight=1)
        self.poster_frame.grid_rowconfigure(0, weight=1)

        self.image2 = Image.open(PATH + "/bg_gradient.png")
        self.image_copy2 = self.image2.copy()
        self.poster_image = ImageTk.PhotoImage(self.image2)

        self.poster_label = customtkinter.CTkLabel(master = self.poster_frame, image = self.poster_image)
        self.poster_label.grid(row = 0, column=0, sticky = "nwse")
        self.poster_label.bind('<Configure>', self.resizeImage)


        #Instructions

        self.instruction_frame = customtkinter.CTkFrame(master=self, corner_radius=0, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = customtkinter.CTkLabel(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = customtkinter.CTkButton(master=self.instruction_frame,
                                                text="Lets Go!",
                                                command=self.button_event)
        self.button.grid(row=1, column=0, sticky= "swe")

    
    def main_screen_0_5(self):

        
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
                                                command=self.button_event_0,
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

    def main_screen_1(self):

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

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(1, weight= 1)



        #Poster

        self.poster_main_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=1, column = 1, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.poster_frame = customtkinter.CTkFrame(master=self.poster_main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_frame.grid(row=0, column = 0, sticky = "nws")
        
        self.poster_frame.grid_columnconfigure(0, weight=1)
        self.poster_frame.grid_rowconfigure(0, weight=1)

        self.image2 = Image.open(PATH + "/bg_gradient.png")
        self.image_copy2 = self.image2.copy()
        self.poster_image = ImageTk.PhotoImage(self.image2)

        self.poster_label = customtkinter.CTkLabel(master = self.poster_frame, image = self.poster_image)
        self.poster_label.grid(row = 0, column=0, sticky = "nwse")
        self.poster_label.bind('<Configure>', self.resizeImage)


        #Frame for main buttons such as Visiting Card and Manually
        self.capture_btn_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.capture_btn_frame.grid(row = 2, column = 1, sticky = "sew")

        self.capture_btn_frame.grid_rowconfigure(0, weight=1)
        self.capture_btn_frame.grid_columnconfigure(0, weight= 1)

        self.visitingCardButton = customtkinter.CTkButton(master=self.capture_btn_frame,
                                                text="Visiting Card",
                                                command=self.button_event_2,
                                                height=50, width=50, padx = 100, pady = 20)
        self.visitingCardButton.grid(row = 0, column = 0, sticky = "sew")

        self.ManualButton = customtkinter.CTkButton(master=self.capture_btn_frame,
                                                text="Manual",
                                                command=self.button_event_2_1,
                                                height=50, width=50, padx = 100, pady = 20)
        self.ManualButton.grid(row = 0, column = 1, sticky = "sew")

        self.capture_btn_frame.grid_rowconfigure(0, weight=1)
        self.capture_btn_frame.grid_columnconfigure(1, weight= 1)

        #Instructions

        self.instruction_frame = customtkinter.CTkFrame(master=self, corner_radius=0, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = customtkinter.CTkLabel(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = customtkinter.CTkButton(master=self.instruction_frame,
                                                text="Back",
                                                command=self.button_event_2_0,
                                                height=50, width=50)
        self.button.grid(row=1, column=0, sticky= "nswe")


    def main_screen_3(self):



        self.video_source = 0

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture2(self.video_source)





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

        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(1, weight= 1)



        #Poster

        self.poster_main_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=1, column = 1, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.poster_frame = customtkinter.CTkFrame(master=self.poster_main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_frame.grid(row=0, column = 0, sticky = "nws")
        
        self.poster_frame.grid_columnconfigure(0, weight=1)
        self.poster_frame.grid_rowconfigure(0, weight=1)

        self.poster_label = customtkinter.CTkLabel(master = self.poster_frame)
        self.poster_label.grid(row = 0, column=0, sticky = "nwse")
        self.poster_label.bind('<Configure>', self.resizeImage)

        #Frame for main buttons such as Visiting Card and Manually
        self.capture_btn_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.capture_btn_frame.grid(row = 2, column = 1, sticky = "sew")

        self.capture_btn_frame.grid_rowconfigure(0, weight=1)
        self.capture_btn_frame.grid_columnconfigure(0, weight= 1)

        self.captureButton = customtkinter.CTkButton(master=self.capture_btn_frame,
                                                text="Click",
                                                command=self.button_event_2,
                                                height=50, width=50, padx = 100, pady = 20)
        self.captureButton.grid(row = 0, column = 0, sticky = "sew")



        #Instructions

        self.instruction_frame = customtkinter.CTkFrame(master=self, corner_radius=0, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = customtkinter.CTkLabel(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = customtkinter.CTkButton(master=self.instruction_frame,
                                                text="Back",
                                                command=self.button_event_2_0,
                                                height=50, width=50)
        self.button.grid(row=1, column=0, sticky= "nswe")


        # After it is called once, the update2 method will be automatically called every delay milliseconds
        self.delay = 15
        self.update2()

        self.mainloop()
        
    def main_screen_4(self): #Registration

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


        #Registration Poster
        yscrollbar = customtkinter.CTkScrollbar(self.main_frame, orientation = "vertical")
        self.reg_frame = customtkinter.CTkFrame(master=self.main_frame, width=180, corner_radius=0, padx = 20, pady = 20)
        self.reg_frame.grid(row=0, column = 0, sticky = "news")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)

        self.reg_label = customtkinter.CTkLabel(master = self.reg_frame, text = "Registration")
        self.reg_label.grid(row = 0, column = 0, sticky = "new")
        self.reg_label.configure(anchor = "center")
        self.reg_frame.grid_columnconfigure(0, weight=1)
        self.reg_frame.grid_rowconfigure(0, weight=1)
        self.reg_frame.grid_rowconfigure(1, weight=4)

        self.det_frame = customtkinter.CTkFrame(master=self.reg_frame, width=180, corner_radius=0, padx = 20, pady = 20)
        self.det_frame.grid(row=1, column = 0, sticky = "news")
        self.det_frame.grid_columnconfigure(0, weight=1)
        self.det_frame.grid_columnconfigure(1, weight=1)
        

        self.name_frame = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 20, pady = 20)
        self.email_frame = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 20, pady = 20)
        self.phone_frame = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 20, pady = 20)
        self.org_frame = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 20, pady = 20)
        self.pov_frame = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 20, pady = 20)

        self.name_frame.grid(row = 0, column = 0)
        self.email_frame.grid(row = 1, column = 0)
        self.phone_frame.grid(row = 2, column = 0)
        self.org_frame.grid(row = 3, column = 0)
        self.pov_frame.grid(row = 4, column = 0)

        self.name_label = customtkinter.CTkLabel(master = self.name_frame, text = "Name")
        self.email_label = customtkinter.CTkLabel(master = self.email_frame, text = "Email")
        self.phone_label = customtkinter.CTkLabel(master = self.phone_frame, text = "Phone")
        self.org_label = customtkinter.CTkLabel(master = self.org_frame, text = "Organisation")
        self.pov_label = customtkinter.CTkLabel(master = self.pov_frame, text = "Purpose of Visit")

        self.name_label.grid(row = 0, column = 0)
        self.email_label.grid(row = 0, column = 0)
        self.phone_label.grid(row = 0, column = 0)
        self.org_label.grid(row = 0, column = 0)
        self.pov_label.grid(row = 0, column = 0)

        self.name_frame2 = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 40, pady = 40)
        self.email_frame2 = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 40, pady = 40)
        self.phone_frame2 = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 40, pady = 40)
        self.org_frame2 = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 40, pady = 40)
        self.pov_frame2 = customtkinter.CTkFrame(master=self.det_frame, width=180, corner_radius=0, padx = 40, pady = 40)

        self.name_frame2.grid(row = 0, column = 1)
        self.email_frame2.grid(row = 1, column = 1)
        self.phone_frame2.grid(row = 2, column = 1)
        self.org_frame2.grid(row = 3, column = 1)
        self.pov_frame2.grid(row = 4, column = 1)

        self.name_text = customtkinter.CTkTextbox(master = self.name_frame2, height=20, width=1000)
        self.email_text = customtkinter.CTkTextbox(master = self.email_frame2, height=20, width=1000)
        self.phone_text = customtkinter.CTkTextbox(master = self.phone_frame2, height=20, width=1000)
        self.org_text = customtkinter.CTkTextbox(master = self.org_frame2, height=20, width=1000)
        self.pov_text = customtkinter.CTkTextbox(master = self.pov_frame2, height=20, width=1000)


        self.name_text.grid(row = 0, column = 0)
        self.email_text.grid(row = 0, column = 0)
        self.phone_text.grid(row = 0, column = 0)
        self.org_text.grid(row = 0, column = 0)
        self.pov_text.grid(row = 0, column = 0)
        

        self.name_text.insert(customtkinter.END, self.list[0])
        self.email_text.insert(customtkinter.END, self.list[2])
        self.phone_text.insert(customtkinter.END, self.list[1])
        self.org_text.insert(customtkinter.END, self.list[3])




        #Frame for S2T and Submit
        self.speak_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.speak_frame.grid(row = 2, column = 0, sticky = "sewn")

        self.speak_frame.grid_rowconfigure(0, weight=1)
        self.speak_frame.grid_columnconfigure(0, weight= 1)

        self.speakButton = customtkinter.CTkButton(master=self.speak_frame,
                                                text="Speak Up!",
                                                command=self.button_event_3,
                                                height=50, width=50, padx = 100, pady = 20)
        self.speakButton.grid(row = 0, column = 0, sticky = "sew")

        self.Submit_Button = customtkinter.CTkButton(master=self.speak_frame,
                                                text="Submit",
                                                command=self.button_event_3_2,
                                                height=50, width=50, padx = 100, pady = 20)
        self.Submit_Button.grid(row = 0, column = 1, sticky = "sew")

        self.speak_frame.grid_rowconfigure(0, weight=1)
        self.speak_frame.grid_columnconfigure(1, weight= 1)

        #Instructions

        self.instruction_frame = customtkinter.CTkFrame(master=self, corner_radius=0, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = customtkinter.CTkLabel(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = customtkinter.CTkButton(master=self.instruction_frame,
                                                text="Back",
                                                height=50, width=50)
        self.button.grid(row=1, column=0, sticky= "nswe")

    def snapshot(self):
        # Get a frame from the video source
        self.ret, frame = self.vid.get_frame()

        if self.ret:
            cv2.imwrite("/home/tejas/Desktop/MySTuff/20-11-2022/target.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update2(self):
        # Get a frame from the video source
        self.ret, frame = self.vid.get_frame()

        if self.ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.poster_label.configure(image = self.photo)

        self.after(self.delay, self.update2)


    def update(self): 
        # Get a frame from the video source
        self.ret, self.frame = self.vid.get_frame()
        if self.ret:
            if self.ret == "alert":
                
                if self.frame == 'Un-identified Face':
                    self.list = ["", "", "", "", ""]
                    self.destroy_window()
                    self.main_screen_3()
                else:
                    self.list = self.frame
                    self.destroy_window()
                    self.main_screen_4()


            elif self.ret: 
                self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(self.frame))
                self.recog_label.configure(image = self.photo)

        self.after(self.delay, self.update)
            

            
  

        #self.cap.release()
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

    
    
    def button_event_0(self):
        y = self.msg_box()
        if y=="yes":
            cv2.destroyAllWindows()
            self.vid.released()
            self.destroy_window()
            self.main_screen()
        else:
            print("No")
        

    def button_event(self):#First Page: Lets Go
        y = self.msg_box()
        if y=="yes":
            self.destroy_window()
            self.main_screen_0_5()
        else:
            print("No")

    def button_event_2_0(self): #Page 2 Back
        y = self.msg_box()
        if y=="yes":
            
            self.destroy_window()
            self.main_screen()
        else:
            print("No")

    def button_event_2(self): #second page for manual settings
        y = self.msg_box()
        if y=="yes":
            cv2.destroyAllWindows()
            self.vid.released()
            self.destroy_window()
            self.main_screen_1()
        else:
            print("No")

    def button_event_2_1(self):
        y = self.msg_box()
        if y=="yes":
            self.destroy_window()
            self.main_screen_4()
        else:
            print("No")

    def button_event_2_2(self):
        self.snapshot()
        y = self.msg_box()
        if y=="yes":
            self.vid.released()
            cv2.destroyAllWindows()
            self.destroy_window()
            self.main_screen_4()
        else:
            print("No")


    
    def text_declaration(self):
        self.x1=self.name_text.textbox.get("1.0", "end-1c")
        self.x2=self.email_text.textbox.get("1.0", "end-1c")
        self.x3=self.phone_text.textbox.get("1.0", "end-1c")
        self.x4=self.org_text.textbox.get("1.0", "end-1c")
        self.x5=self.pov_text.textbox.get("1.0", "end-1c")

    def button_event_3(self):
        # name email phone org pov
        
        
        self.text_declaration()
        y=self.speechToTextFn()
        if self.x1 == "":
            self.name_text.insert(customtkinter.END, y)
            self.x1 = y


        elif self.x2 == "":
            y = y.split(" ")
            y = "".join(y)
            y = y.lower()
            y = y.split("at")
            y = "@".join(y)
            y = y.split("dot")
            y = ".".join(y)
            self.email_text.insert(customtkinter.END, y)
            self.x2 = y

        elif self.x3 == "":
            self.phone_text.insert(customtkinter.END, y)
            self.x3 = y

        elif self.x4 == "":
            self.org_text.insert(customtkinter.END, y)
            self.x4 = y

        elif self.x5 == "":
            self.pov_text.insert(customtkinter.END, y)
            self.x5 = y

        else:
            pass


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

    def button_event_3_1(self):
        y = self.msg_box()
        if y=="yes":
            self.vid.released()
            cv2.destroyAllWindows()
            self.destroy_window()
            self.main_screen_4()
        else:
            print("No")

    def button_event_3_2(self): #Final Submit
        y = self.msg_box()
        if y=="yes":
            self.text_declaration()
            self.pdf_create()
            self.destroy_window()
            self.main_screen()
        else:
            print("No")


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

    



class MyVideoCapture:

    def __init__(self, video_source=0):
        # Open the video source
        os.chdir(r'/home/tejas/Desktop/MySTuff/20-11-2022/Face Recognition/Celebrity Images')
        self.df=pd.read_csv('/home/tejas/Desktop/MySTuff/20-11-2022/Data.csv')
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



class MyVideoCapture2:
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









if __name__ == "__main__":
    app = App()
    app.mainloop()
