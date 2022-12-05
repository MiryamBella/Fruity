import requests
from pyquery import PyQuery as pq
import json
import codecs


import DataFromWeb as webData


#get html from website.
response = requests.get('https://www.kosharot.co.il/index2.php?id=7&lang=HEB')
html = pq(response.text)
#get the data of the fruits.
divs = html.find("div")
div = webData.getClassObject(divs, "page3_table_contant")

fruits = webData.getDataAsList(div, "https://www.kosharot.co.il/")

print(webData.enrichData(fruits[22]), "page7_table_data")

#getText()

webData.saveDataAsJson("fruitsList.json", fruits)
#webData.saveDataAstext("fruitsList.txt", fruits)
#print(fruits)

webData.getDataFromJyson("fruitsList.json")
