
import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()



if __name__ == "__main__":
    app = App()
    app.mainloop()

