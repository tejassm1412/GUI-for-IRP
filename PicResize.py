import tkinter as tk
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

PATH = os.path.dirname(os.path.realpath(__file__))

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Title")
        
        

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.frame_left = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)


        self.frame_right = customtkinter.CTkFrame(master=self, width=180, corner_radius=0, padx = 20, pady = 20)

        self.frame_left.grid(row = 0, column=0, sticky = "nws")

        self.frame_right.grid(row = 0, column=1, sticky = "nwse")

        self.button_1 = customtkinter.CTkButton(master = self.frame_left, text = "Button", command= self.done)
        self.button_1.grid(row=0, column=0, padx = 20, pady = 20)


        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=1)


        self.image = Image.open(PATH + "/bg_gradient.png")
        self.image_copy = self.image.copy()
        self.bg_image = ImageTk.PhotoImage(self.image)

        


        self.label_1 = customtkinter.CTkLabel(master = self.frame_right, image = self.bg_image)
        self.label_1.grid(row = 0, column=0, sticky = "nwse")

        self.label_1.bind('<Configure>', self.resizeImage)

    def done(self):
        self.frame_left.destroy()

    def resizeImage(self, event):
        image = self.image_copy.resize(
            (self.frame_right.winfo_width(), self.frame_right.winfo_height()))
        self.newimage = ImageTk.PhotoImage(image)
        self.label_1.configure(image = self.newimage)

        


if __name__ == "__main__":
    app = App()
    app.mainloop()
