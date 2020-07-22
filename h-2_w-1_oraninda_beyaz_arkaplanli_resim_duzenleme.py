import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory
import re
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

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
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
        #out = cv2.imread(ImageFilePath,0)
        #out = image_resize(out, width = wi, height = hi, inter = cv2.INTER_AREA)
        #cv2.imwrite(ImageFilePath,out)
        #cv2.imshow("resize", out)
        #cv2.waitKey(0)
    
    elif(width < height and height < (2 * width)):
        bigside = width
        bgs = width * 2

        background = Image.new('RGB', (bigside, bgs), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bgs - height) / 2),0)))

        background.paste(image, offset)
        background = background.convert('RGB')
        background.save(ImageFilePath)
        print("Image has been resized !")
        #out = cv2.imread(ImageFilePath,0)
        #out = image_resize(out, width = wi, height = hi, inter = cv2.INTER_AREA)
        #cv2.imwrite(ImageFilePath,out)
        #cv2.imshow("resize", out)
        #cv2.waitKey(0)
    
    elif(width < height and height > (2*width)):
        bigside = int(height / 2)
        bgs = 2* bigside

        background = Image.new('RGB', (bigside, bgs), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bgs - height) / 2),0)))

        background.paste(image, offset)
        background = background.convert('RGB')
        background.save(ImageFilePath,0)
        print("Image has been resized !")
        #out = cv2.imread(ImageFilePath)
        #out = image_resize(out, width = wi, height = hi, inter = cv2.INTER_AREA)
        #cv2.imwrite(ImageFilePath,out)
        #cv2.imshow("resize", out)
        #cv2.waitKey(0)

    else:
        print("Image is already a proper, it has not been resized !")

def inp():
    try:
        global hi
        global wi
        
        hi = None
        wi = None
        hw = str(input("Yükseklik mi yoksa genişlik üzerinden mi ölçeklendirme yapmak istersiniz (1 / 2)? (Yükseklik için 1, genişlik için 2 giriniz)"))
        #dm = int(input("Ölçek değerini giriniz!"))
        #if re.match(r'[1]{1}',dm) and not re.match(r'([1]{1})([0-9a-zA-Z-_?./\\\'"*+|%&$#£>é<]{1,})',dm):
        
        #if hw == "1":
        #    hi = dm
        #if hw == "2":
        #    wi = dm
        #print(dm,hw,hi,wi)
    except:
        print("Lütfen geçerli bir parametre giriniz!!!")
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
path = askdirectory(title = "İsimleri düzenlenecek resimlerin bulunduğu ana klasörü seçiniz!")
#print(path)

#inp()
scan(path)
