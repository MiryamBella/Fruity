import requests
from pyquery import PyQuery as pq
import json
import codecs


import DataFromWeb as webData


def getData(link, className):
    response = requests.get(link)
    html = pq(response.text)
    # get the data of the fruits.
    table = html.find("div")
    a=table.getElementById("pageHeader")
    kid=webData.getClassObject(table,"col-lg-12")
    print(kid)
    a= webData.getClassObject(kid,"col - 12")

    return a
class Foodsdictionary:
    def __init__(self, nameFile):
        self.linksInfo = webData.getDataFromJyson(nameFile)
        if (self.linksInfo == None):
            self.linksInfo = self.makeData(nameFile)

    def get_f(self):
        return self.linksInfo

    def __str__(self):
        return f"{self.linksInfo}"

    def makeData(self, nameFile):
        # get html from website.
        response = requests.get('https://www.foodsdictionary.co.il/articles/875')
        html = pq(response.text)
        # get the data of the fruits.
        table = html.find("table")

        myTable = webData.getClassObject(table, "textTable")
        ul = myTable.find("tbody").find("tr").find("td").find("ul")

        links = webData.getDataAsList(ul, '')
        webData.saveDataAsJson(nameFile, links)
        return links


'''
response = requests.get('https://www.foodsdictionary.co.il/articles/875')
html = pq(response.text)
#get the data of the fruits.
table = html.find("table")

myTable = webData.getClassObject(table, "nv-table")
#td= myTable.find("tbody").find("tr").find("td")
print(table)
'''

dataFood= Foodsdictionary("jsonFiles/foodsdictionary_info.json")

print(dataFood)
#print(getData(links[0]['link'], "col-12"))
#print(webData.enrichData(fruits[22]))

#getText()
'''
webData.saveDataAsJson("fruitsList.json", fruits)
#webData.saveDataAstext("fruitsList.txt", fruits)
#print(fruits)

webData.getDataFromJyson("fruitsList.json")
'''
