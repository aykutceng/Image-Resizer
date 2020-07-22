import cv2
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import re
from PIL import Image
# load the image and show it
# image = cv2.imread("650x344-deneme-nedir-ve-nasil-yazilir-1540990804971.jpg")
# print(image.shape)
# cv2.imshow("original", image)
# cv2.waitKey(0)

# cropped = image[0:800, 0:650]
# cv2.imshow("resize", cropped)
# cv2.waitKey(0)


hi = None
wi = None

""" def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    try:
        dim = (int(width), int(height))
        resized = cv2.resize(image, dim, interpolation = inter)
        return resized
    except:
        return False """

def RS(ImageFilePath,name):
    global hi
    global wi
    try:
        dim = (wi,hi)
        image = Image.open(ImageFilePath, 'r')
        image_size = image.size
        width = image_size[0]
        height = image_size[1]
        background = Image.new('RGBA', dim, (255, 255, 255, 255))
        image = image.resize(dim)
        background.paste(image, (0,0))
        background = background.convert('RGB')
        background.save(ImageFilePath)
        print("Image has been resized !")
    except Exception as e:
        print(str(e))

def inp():
    try:
        global hi
        global wi
        
        hi = int(input("Please enter height!"))
        wi = int(input("Please enter width!"))
        if hi < 1 or wi < 1:
            print("Please enter integer only! Zero (0) is not allowed!")
            return inp()
        

    except:
        print("Please enter a valid parameter!!!")
        return inp()


def scan(path):
    with os.scandir(path) as listOfEntries:
        for entry in listOfEntries:
            
            if entry.is_dir():
                #print(path)
                scan(path+'/'+entry.name)
            else:
                if re.search(".*.png$", entry.name) or re.search(".*.jpeg$", entry.name) or re.search(".*.jpg$", entry.name):
                    RS(path+'/'+entry.name,entry.name)
                    #print(path+'/'+entry.name)


Tk().withdraw()
path = askdirectory(title = "Choose parent folder which contains sub folders and images!")
#print(path)

inp()
scan(path)
