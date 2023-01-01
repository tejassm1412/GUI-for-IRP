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
        self.window1()
        
    def window1(self):
        self.title("Title")
        self.frame = customtkinter.CTkFrame(master=self, corner_radius=0, padx=20, pady=20, fg_color="red")
        self.frame.grid(row = 0, column = 0, sticky = "news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.button = customtkinter.CTkButton(master = self.frame, text = "Button", padx = 100, pady = 100, command = self.next)
        self.button.grid(row = 1, column = 0, sticky = "news")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)

    def next(self):
        for widgets in self.winfo_children():
            widgets.destroy()

        self.title("Title")
        self.frame = customtkinter.CTkFrame(master=self, corner_radius=0, padx=20, pady=20, fg_color="blue")
        self.frame.grid(row = 0, column = 0, sticky = "news")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.button = customtkinter.CTkButton(master = self.frame, text = "Button", padx = 50, pady = 50, command = self.window1)
        self.button.grid(row = 1, column = 0, sticky = "news")
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)




        



if __name__ == "__main__":
    app = App()
    app.mainloop()
