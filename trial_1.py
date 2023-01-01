import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os
import time
import cv2
from simple_facerec import SimpleFacerec
import dlib
import os
import pytesseract

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))


class App(customtkinter.CTk):


    def __init__(self):
        super().__init__()

        self.title("Maya Gui")

        self.attributes('-zoomed', True)
        self.main_screen_2()
        self.i = 0
        self.y1 = ""
        self.y2 = ""
        self.y3 = ""
        self.y4 = ""

    def main_screen_2(self):

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

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight= 1)



        #Poster

        self.poster_main_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.poster_main_frame.grid(row=0, column = 0, sticky = "nwes")

        self.poster_main_frame.grid_columnconfigure(0, weight=1)
        self.poster_main_frame.grid_rowconfigure(0, weight=1)

        self.ocr_text_frame = customtkinter.CTkFrame(master=self.poster_main_frame, corner_radius=0, padx = 20, pady = 20)
        self.ocr_text_frame.grid(row=0, column = 0, sticky = "ns")
        
        self.ocr_text_frame.grid_columnconfigure(0, weight=1)
        self.ocr_text_frame.grid_rowconfigure(0, weight=1)

        self.ocr_text = customtkinter.CTkTextbox(master = self.ocr_text_frame, height=20, width=1000)
        self.ocr_text.grid(row = 0, column = 0, sticky = "ew")

        self.radio_frame = customtkinter.CTkFrame(master=self.poster_main_frame, corner_radius=0, padx = 20, pady = 20)
        self.radio_frame.grid(row=1, column = 0, sticky = "ns")

        self.radio_var = customtkinter.IntVar()


        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=0, text="Name")
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=1, text="Email")
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=2, text="Phone")
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=3, text="Organisation")
        self.radio_button_4.grid(row=4, column=0, pady=10, padx=20, sticky="nw")

        self.radio_button_5 = customtkinter.CTkRadioButton(master=self.radio_frame,
                                                           variable=self.radio_var,
                                                           value=4, text="Skip")
        self.radio_button_5.grid(row=5, column=0, pady=10, padx=20, sticky="nw")



        #Frame for main buttons such as Visiting Card and Manually
        self.buttons_frame = customtkinter.CTkFrame(master=self.main_frame, corner_radius=0, padx = 20, pady = 20)
        self.buttons_frame.grid(row = 1, column = 0, sticky = "sew")

        self.buttons_frame.grid_rowconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(0, weight= 1)

        self.submit_Button = customtkinter.CTkButton(master=self.buttons_frame,
                                                text="Next",
                                                command=self.button_event,
                                                height=50, width=50, padx = 100, pady = 20)
        self.submit_Button.grid(row = 0, column = 0, sticky = "sew")


        


        #Instructions

        self.instruction_frame = customtkinter.CTkFrame(master=self, corner_radius=0, padx = 20, pady = 20)
        self.instruction_frame.grid(row=1, column = 0, sticky = "nwes")

        self.instructions = customtkinter.CTkLabel(master = self.instruction_frame, 
                                                    text= "Instructions\nChoose what field the info\nbelongs to.\n\nSkip in case:\nInfo is irrelevant\nInfo is Blank\n\n", 
                                                    padx = 20, pady = 20)
        self.instructions.grid(row = 0, column=0, sticky = "nwse")

        self.instruction_frame.grid_columnconfigure(0, weight=1)
        self.instruction_frame.grid_rowconfigure(0, weight=1)




        self.button = customtkinter.CTkButton(master=self.instruction_frame,
                                                text="Back",
                                                command=self.button_event,
                                                height=50, width=50)
        self.button.grid(row=1, column=0, sticky= "nswe")
        self.reset()
        self.ocr_recognise()
        

    def reset(self):
        self.x1 = ""
        self.x2 = ""
        self.x3 = ""
        self.x4 = ""
        self.x5 = ""

    

    def ocr_recognise(self):
        self.img = cv2.imread('target2.jpg')

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

    def button_event(self):
        self.data_match()
        self.destroy_window()
        self.main_screen_2()
        self.ocr_text.insert(customtkinter.END, self.ocrs[self.i])
        
        self.i += 1
        print(self.i)
        print(len(self.ocrs))
        

        if self.i >= len(self.ocrs):
            self.ocr_text.insert(customtkinter.END, "Done")
            self.i = 0
            print("Strings Are:", self.y1, self.y2, self.y3, self.y4)
            print("y1 =", self.y1, "\n", "y2 =", self.y2, "\n", "y3 =", self.y3, "\n", "y4 =", self.y4, "\n", )
            self.destroy_window()

        

    

    def data_match(self):
        self.rv = self.get_radio()
        self.boxVal = self.ocr_text.textbox.get("1.0", "end-1c")
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

if __name__ == "__main__":
    app = App()
    app.mainloop()
