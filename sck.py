import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import cv2
plt.style.use('seaborn')
from tkinter import filedialog
from tkinter import *
import skimage 
import array
root = Tk()
root.title("Sketched")

ClickChecker = False
def skectched(image):
    grey_img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    invert_img = cv2.bitwise_not(grey_img)
    blur_img = cv2.GaussianBlur(invert_img, (111,111),0)
    invertedblur = cv2.bitwise_not(blur_img)
    sketch_img = cv2.divide(grey_img,invertedblur,scale= 256.0)
    return sketch_img



def file_opener(a=0):
    global ClickChecker
    global fileN

    if a == 0:
        ClickChecker = True

        fileName = filedialog.askopenfile(mode='r', filetypes=[('Image files', '*.jpg'), ('Image files(png)', '*.png'), ('Image files', '*.jpeg') ])
        if fileName is not None:
            print(fileName.name)
            fileN = fileName.name

            entry["width"] = len(fileN) - 20
            entry.insert(0, fileN)
            button1["state"] = NORMAL
    elif a == 1:

        print(fileN)
        img = cv2.imread(fileN)
        RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        print(b_w_checker.get(), aqua_checker.get(), sepia_checker.get(), sketch_checker.get(), vintage_checker.get())
        if sketch_checker.get() == 1:
            sketched_image = skectched(RGB_img)
            plt.imshow(sketched_image)
            plt.axis(False)
            plt.show()
        else:
            plt.imshow(RGB_img)
            plt.axis(False)
            plt.show()
        
def function(Test):
    print("Hi this is a test", Test)

function('a')
button = Button(root, text="Browse", command=file_opener, width=5, height=1)
button.grid(column=4, row=1)
button1 = Button(root, text="Convert", command=lambda: file_opener(1), state=DISABLED, width=5, height=1)

button1.grid(column=2, row=2)

entry = Entry(root, background="white", borderwidth=2,
              width=len("/Users/rohitkumar/Downloads/Wallpaper/wallpaperflare.com_wallpaper-2 copy.jpg") - 20,
              fg="black")

entry.grid(column=0, row=1, columnspan=4)

b_w_checker = IntVar()
aqua_checker = IntVar()
sepia_checker = IntVar()
vintage_checker = IntVar()
sketch_checker = IntVar()

b_w = Checkbutton(root, text="B&W", variable=b_w_checker)
b_w.grid(row=0, column=0)

aqua = Checkbutton(root, text="AQUA", variable=aqua_checker)
aqua.grid(row=0, column=1)

sketch = Checkbutton(root, text="SKETCH", variable=sketch_checker)
sketch.grid(row=0, column=2)

sepia = Checkbutton(root, text="SEPIA", variable=sepia_checker)
sepia.grid(row=0, column=3)

vintage = Checkbutton(root, text="VINTAGE", variable=vintage_checker)
vintage.grid(row=0, column=4)
root.mainloop()
