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
div = webData.getDataDiv(divs, "page3_table_contant")

fruits = webData.getData(div)

#print(webData.enrichData(fruits[22]))

#getText()

webData.saveDataAsJson("fruitsList.json", fruits)
#webData.saveDataAstext("fruitsList.txt", fruits)
#print(fruits)

webData.getDataFromJyson("fruitsList.json")