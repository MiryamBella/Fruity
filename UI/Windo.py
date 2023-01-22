from bs4 import BeautifulSoup
import BL.IdentifyModel as idClass
import os
from pyquery import PyQuery as pq
import DAL.web_data.DataFromKosharot as kosarot
import DAL.web_data.DataFromFoodsdictionary as dataofFruits
import DAL.web_data.DataFromFruitAcademy as recapis
from bs4 import BeautifulSoup as bs
import os
import re
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
        '''with open(os.path.join(instance_path,"UI/form.html"), "r", encoding='utf-8') as f:
            text = f.read()'''
        #self.htmlPage ={"main": text}
        self.kosharot= kosarot.cosharot(os.path.join(instance_path,"DAL/web_data/jsonFiles/fruitsList.json"))
        self.dataofFruits = dataofFruits.Foodsdictionary_data(os.path.join(instance_path,"DAL/web_data/jsonFiles/foodsdictionary_info.json"))
        self.recepies =recapis.FoodsdictionaryRecipe(os.path.join(instance_path,"DAL/web_data/jsonFiles/fruitAcademy_recipe.json"))



    def idetifyImage(self, nameImage, instance_path=""):
        nameObject= self.myIdenify.identifyObject(nameImage)
        #nameObject = self.myIdenify.translateNameFruit2hebrew(nameObject)

        '''
        # Open the HTML in which you want to make changes
        html = open(os.path.join(instance_path, 'UI/page2.html'))
        # Parse HTML file in Beautiful Soup
        soup = bs(html, 'html.parser')
        # Give location where text is stored which you wish to alter
        old_text = soup.find("p", {"id": "nameFruit"})
        # Replace the already stored text with the new text which you wish to assign
        new_text = old_text.find(text=re.compile('')).replace_with(nameObject)
        # Alter HTML file to see the changes done
        with open("gfg.html", "wb") as f_output:
            f_output.write(soup.prettify("utf-8"))
        self.htmlPage["idtify": new_text]
        '''
        return nameObject

    def getRecipients(self, name):
        return self.recepies.getRecipe_byNameComponet(name)

    def getDataFruites(self, name):
        return self.dataofFruits.GetData_ByName(name)

    def getData_cosharot(self, name):
        return self.kosharot.getFruite(name)



    def translateNameFruit2hebrew(self, eName):
        dicthenery= {"apple": "תפוח", "avocado": "אבוקדו", "banana": "בננה", "cherry": "דובדבן", "kiwi": "קיווי",
                     "mango": "מנגו", "orange": "תפוז", "pinenapple": "אננס", "strawberries": "תות", "watermelon": "אבטיח"}
        resukt= dicthenery[eName]
        return resukt

