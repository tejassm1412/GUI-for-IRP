import customtkinter
import cv2
import PIL.Image, PIL.ImageTk
import time


class App2(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Maya Gui")

        self.attributes('-zoomed', True)
        self.main_screen_3()

    def main_screen_3(self):

        self.title("title")
        self.video_source = 0

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture2(self.video_source)
        
        self.top_frame = customtkinter.CTkFrame(self, padx = 20)
        self.top_frame.grid(row = 0, column = 0, sticky = "news")

        # Create a canvas that can fit the above video source size
        self.canvas = customtkinter.CTkLabel(self.top_frame, width = self.vid.width, height = self.vid.height, anchor = "center")
        self.canvas.grid(row=0, column=0, sticky = "ns")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_rowconfigure(0, weight=1)

        # Button that lets the user take a snapshot
        self.btn_snapshot=customtkinter.CTkButton(self, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.grid(row=1, column=0, sticky = "news")

        # After it is called once, the update2 method will be automatically called every delay milliseconds
        self.delay = 15
        self.update2()

        self.mainloop()
        

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update2(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.configure(image = self.photo)

        self.after(self.delay, self.update2)

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
            ret, frame = self.vid.read()
            frame_2 = self.rescale_frame(frame, percent = 200)
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame_2, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the Application object
App2()