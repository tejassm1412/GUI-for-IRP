import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import os
import time
import cv2
from simple_facerec import SimpleFacerec
import dlib
import os
import random as rand
from threading import *

PATH = os.path.dirname(os.path.realpath(__file__))


class App(tkinter.Tk):


    def __init__(self):
        super().__init__()
        self.title("Maya Gui")

        self.attributes('-zoomed', True)
        self.main_screen_4()

    def main_screen_4(self):
        self.config(bg="white")
        #main Container
        self.main_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, bg = "white")
        self.main_frame.grid(row=1, column = 1, sticky = "news")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        #logo
        self.logo_frame = tkinter.Frame(master=self, width=180, padx = 20, pady = 20, bg = "white")
        self.logo_frame.grid(row=0, column = 0, sticky = "news")

        self.image = Image.open(PATH + "/kle.png").resize((500, 100))
        self.logo_image = ImageTk.PhotoImage(self.image)
        self.logo_label = tkinter.Label(master = self.logo_frame, image = self.logo_image, bg = "white")
        self.logo_label.grid(row = 0, column=0, sticky = "nwse")

        #PosterConfig GRID

        self.main_frame.rowconfigure(1, weight=1)
        
        self.main_frame.columnconfigure(0, weight=2)

        #Registration Poster
        self.reg_frame = tkinter.Frame(master=self.main_frame)
        self.reg_frame.grid(row=0, column = 0, sticky = "news")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.reg_label = tkinter.Label(master = self.reg_frame, text = "REGISTRATION", padx = 30,  pady = 30, bg = "#F5F5F5", font=("Montserrat", 25))
        self.reg_label.grid(row = 0, column = 0, sticky = "new")
        self.reg_label.configure(anchor = "center")
        self.reg_frame.columnconfigure(0, weight=1)
        self.reg_frame.rowconfigure(0, weight=1)
        self.reg_frame.rowconfigure(1, weight=4)

        self.det_frame = tkinter.Frame(master=self.reg_frame, width=180, padx = 20, pady = 20, bg = "white")
        self.det_frame.grid(row=1, column = 0, sticky = "news")
        self.det_frame.columnconfigure(0, weight=1)
        self.det_frame.columnconfigure(1, weight=1)

        self.name_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20, bg = "white")
        self.email_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20, bg = "white")
        self.phone_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20, bg = "white")
        self.org_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20, bg = "white")
        self.pov_frame = tkinter.Frame(master=self.det_frame, width=180, padx = 20, pady = 20, bg = "white")

        
        self.name_frame.grid(row = 0, column = 0)
        self.email_frame.grid(row = 1, column = 0)
        self.phone_frame.grid(row = 2, column = 0)
        self.org_frame.grid(row = 3, column = 0)
        self.pov_frame.grid(row = 4, column = 0)

        

        self.name_label = tkinter.Label(master = self.name_frame, text = "NAME", bg = "white", font=("Arial", 20))
        self.email_label = tkinter.Label(master = self.email_frame, text = "EMAIL", bg = "white", font=("Arial", 20))
        self.phone_label = tkinter.Label(master = self.phone_frame, text = "PHONE", bg = "white", font=("Arial", 20))
        self.org_label = tkinter.Label(master = self.org_frame, text = "ORGANISATION", bg = "white", font=("Arial", 20))
        self.pov_label = tkinter.Label(master = self.pov_frame, text = "PURPOSE OF VISIT", bg = "white", font=("Arial", 20))

        

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

        

        self.name_text = tkinter.Text(master = self.name_frame2, height = 2, font=("Arial", 12))
        self.email_text = tkinter.Text(master = self.email_frame2, height = 2, font=("Arial", 12))
        self.phone_text = tkinter.Text(master = self.phone_frame2, height = 2, font=("Arial", 12))
        self.org_text = tkinter.Text(master = self.org_frame2, height = 2, font=("Arial", 12))
        self.pov_text = tkinter.Text(master = self.pov_frame2, height = 2, font=("Arial", 12))



        self.name_text.grid(row = 0, column = 0)
        self.email_text.grid(row = 0, column = 0)
        self.phone_text.grid(row = 0, column = 0)
        self.org_text.grid(row = 0, column = 0)
        self.pov_text.grid(row = 0, column = 0)


        #Frame for S2T and Submit
        self.speak_frame = tkinter.Frame(master=self.main_frame, padx = 20, pady = 20, bg = "white")
        self.speak_frame.grid(row = 2, column = 0, sticky = "sewn")

        self.speak_frame.rowconfigure(0, weight=1)
        self.speak_frame.columnconfigure(0, weight= 1)


        self.visitingCardButton = tkinter.Button(master=self.speak_frame,
                                                text="Speak Up!",
                                                command=self.button_event,
                                                padx = 20, pady = 20, bg = "white")
        self.visitingCardButton.grid(row = 0, column = 0, sticky = "sew")

        self.Submit_Button = tkinter.Button(master=self.speak_frame,
                                                text="Submit",
                                                command=self.button_event,
                                                padx = 20, pady = 20, bg = "white")
        self.Submit_Button.grid(row = 0, column = 1, sticky = "sew")

        self.speak_frame.rowconfigure(0, weight=1)
        self.speak_frame.columnconfigure(1, weight= 1)



        #Instructions

        self.instruction_frame = tkinter.Frame(master=self, padx = 20, pady = 20, bg = "white")
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = tkinter.Label(master = self.instruction_frame, text= "Instructions come heregfdytdutldigfuylfiyfuyc", padx = 20, pady = 20, bg = "#F5F5F5")
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.columnconfigure(0, weight=1)
        self.instruction_frame.rowconfigure(0, weight=1)




        self.button = tkinter.Button(master=self.instruction_frame,
                                                text="Back", bg="#0096FF")
        self.button.grid(row=1, column=0, sticky= "swe")

    def button_event(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()