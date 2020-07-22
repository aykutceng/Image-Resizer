import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import re

hi = None
wi = None

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)

    return resized


def RS(ImageFilePath,name):
    global hi
    global wi

             
            
    from PIL import Image
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width >= height):
        bigside = width
        bgs = width * 2

        background = Image.new('RGBA', (bigside, bgs), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bgs - height) / 2),0)))

        background.paste(image, offset)
        background = background.convert('RGB')
        background.save(ImageFilePath)
        print("Image has been resized !")
    
    elif(width < height and height < (2 * width)):
        bigside = width
        bgs = width * 2

        background = Image.new('RGB', (bigside, bgs), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bgs - height) / 2),0)))

        background.paste(image, offset)
        background = background.convert('RGB')
        background.save(ImageFilePath)
        print("Image has been resized !")
    
    elif(width < height and height > (2*width)):
        bigside = int(height / 2)
        bgs = 2* bigside

        background = Image.new('RGB', (bigside, bgs), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bgs - height) / 2),0)))

        background.paste(image, offset)
        background = background.convert('RGB')
        background.save(ImageFilePath,0)
        print("Image has been resized !")

    else:
        print("Image is already a proper, it has not been resized !")

def inp():
    try:
        global hi
        global wi
        
        hi = None
        wi = None
        hw = str(input("Which property do you want to use to resize images? 1 for height, 2 for width"))

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
path = askdirectory(title = "Please choose parent folder which contains sub folders and images!")
#print(path)

#inp()
scan(path)
