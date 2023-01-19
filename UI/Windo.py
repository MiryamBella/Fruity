from bs4 import BeautifulSoup
import BL.IdentifyModel as idClass
import os
from pyquery import PyQuery as pq
#import cv2

'''
    def takepoto(self):
        camera = cv2.VideoCapture(0)
        eturn_value, image = camera.read()
        name= str(self.runNum)+'.png'
        self.runNum+=1
        cv2.imwrite("../DAL/dataset/clientsImage/"+ name, image)
        del (camera)
        return name
'''


class Menu:
    def __init__(self, instance_path=""):
        self.runNum=0
        self.myIdenify = idClass.Identify()
        with open(os.path.join(instance_path,"UI/form.html"), "r", encoding='utf-8') as f:
            text = f.read()
        self.htmlPage ={"main": text}




    def idetifyImage(self, nameImage):
        nameObject= self.myIdenify.identifyObject(nameImage)
        nameObject = self.myIdenify.translateNameFruit2hebrew(nameImage)
        return nameImage

    def mainPageAsStr(self):
        return self.htmlPage["main"]

    def resultIdetify(self, nameObject, instance_path=""):
        with open(os.path.join(instance_path,"UI/page2.html"), "r", encoding='utf-8') as f:
            text = f.read()

        from bs4 import BeautifulSoup as bs
        import os
        import re

        # Remove the last segment of the path
        base = os.path.dirname(os.path.abspath(__file__))

        # Open the HTML in which you want to make changes
        html = open(os.path.join(base, 'UI/page2.html'))

        # Parse HTML file in Beautiful Soup
        soup = bs(html, 'html.parser')

        # Give location where text is
        # stored which you wish to alter
        old_text = soup.find("p", {"id": "para"})

        # Replace the already stored text with
        # the new text which you wish to assign
        new_text = old_text.find(text=re.compile(
            'Geeks For Geeks')).replace_with('Vinayak Rai')

        # Alter HTML file to see the changes done
        with open("gfg.html", "wb") as f_output:
            f_output.write(soup.prettify("utf-8"))






