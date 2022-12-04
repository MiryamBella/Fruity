import requests
from pyquery import PyQuery as pq
import json
import codecs


import DataFromWeb as webData


#get html from website.
response = requests.get('https://www.foodsdictionary.co.il/articles/875')
html = pq(response.text)
#get the data of the fruits.
table = html.find("table")

myTable = webData.getDataDiv(table, "textTable")
ul= myTable.find("tbody").find("tr").find("td").find("ul")

fruits = webData.getData(ul, '')
print(fruits)
#print(webData.enrichData(fruits[22]))

#getText()
'''
webData.saveDataAsJson("fruitsList.json", fruits)
#webData.saveDataAstext("fruitsList.txt", fruits)
#print(fruits)

webData.getDataFromJyson("fruitsList.json")
'''