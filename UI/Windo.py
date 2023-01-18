

from guizero import App, Text, PushButton
'''
app = App(title="guizero")
hebro="gvg"
butti="knjk"
intro = Text(app, text=hebro)
ok = PushButton(app, text=butti)

app.display()

# program to capture single image from webcam in python

# importing OpenCV library
import cv2

# initialize the camera
# If you have multiple camera connected with
# current device, assign a value in cam_port
# variable according to that
cam_port = 0
cam = cv2.VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error,
# show result
if result:

    # showing result, it take frame name and image
    # output
    cv2.imshow("GeeksForGeeks", image)

    # saving image in local storage
    cv2.imwrite("GeeksForGeeks.png", image)

    # If keyboard interrupt occurs, destroy image
    # window
    #cv2.waitKey(0)
    #cv2.destroyWindow("GeeksForGeeks")

# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")

'''
import BL.IdentifyModel as idClass
import cv2


class Menu:
    def __init__(self):
        self.runNum=0
        self.myIdenify = idClass.Identify()
        print("welcom")

    def takepoto(self):
        camera = cv2.VideoCapture(0)
        eturn_value, image = camera.read()
        name= str(self.runNum)+'.png'
        self.runNum+=1
        cv2.imwrite("../DAL/dataset/clientsImage/"+ name, image)
        del (camera)
        return name

    def idetifyImage(self, nameImage):
        nameObject= self.myIdenify.identifyObject(nameImage)
        nameObject = self.myIdenify.translateNameFruit2hebrew(nameImage)
        return nameImage









