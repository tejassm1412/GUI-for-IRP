import pytesseract
import cv2
def ocr_recognise():
    img = cv2.imread('/home/tejas/Desktop/MySTuff/20-11-2022/ktp3.jpg')

    img = cv2.resize(img, (600, 360))
    x = pytesseract.image_to_string(img)
    print(x)
    
    y = x.split("\n")
    z = []
    for x in y:
        if x != '' and x!= "\x0c":
            z.append(x)

    print(z)

ocr_recognise()