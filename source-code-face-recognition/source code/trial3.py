import cv2
from simple_facerec import SimpleFacerec
import dlib
import os
import numpy
from tkinter import *
from PIL import Image, ImageTk
import datetime

def Photolelo():
    image = Image.fromarray(img1)
    time = str(datetime.datetime.now().today()).replace(":", " ")+".jpg"
    image.save(time)



# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("/home/tejas/Desktop/MySTuff/20-11-2022/source-code-face-recognition/source code/images")

# Load Camera
cap = cv2.VideoCapture(0)


for i in range(1):
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

print(frame.shape)
while True:
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()



root = Tk()
root.geometry("700x540")

root.configure(bg = "black")
Label(root, text = "Camera App", font = ("times new roman", 30, "bold")).pack()
f1 = LabelFrame(root, bg = "red")
f1.pack()
L1 = Label(f1, bg = "red")
L1.pack()
cap = cv2.VideoCapture(0)
Button(root, text = "Take Snap", command=Photolelo).pack()
while True:
    img = cap.read()[1]
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img
    root.update()

cap.release()