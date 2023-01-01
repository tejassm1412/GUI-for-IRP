import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
import time
import cv2
import dlib
import os

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


class App(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.title("Maya Gui")

        self.attributes('-zoomed', True)
        self.main_screen_1()

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
        self.visiting_card_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.visiting_card_frame.grid(row = 2, column = 1, sticky = "sew")

        self.visiting_card_frame.grid_rowconfigure(0, weight=1)
        self.visiting_card_frame.grid_columnconfigure(0, weight= 1)

        self.visitingCardButton = customtkinter.CTkButton(master=self.visiting_card_frame,
                                                text="Visiting Card",
                                                command=self.button_event,
                                                height=50, width=50, padx = 100, pady = 20)
        self.visitingCardButton.grid(row = 0, column = 0, sticky = "sew")

        self.ManualButton = customtkinter.CTkButton(master=self.visiting_card_frame,
                                                text="Manual",
                                                command=self.button_event,
                                                height=50, width=50, padx = 100, pady = 20)
        self.ManualButton.grid(row = 0, column = 1, sticky = "sew")

        self.visiting_card_frame.grid_rowconfigure(0, weight=1)
        self.visiting_card_frame.grid_columnconfigure(1, weight= 1)

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

        



    def button_event(self):
        pass


    def resizeImage(self, event):
        image = self.image_copy2.resize(
            (self.poster_frame.winfo_width(), self.poster_frame.winfo_height()))
        self.newimage = ImageTk.PhotoImage(image)
        #print(self.poster_frame.winfo_width(), self.poster_frame.winfo_height())
        self.poster_label.configure(image = self.newimage)




        cv2.destroyAllWindows()
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
