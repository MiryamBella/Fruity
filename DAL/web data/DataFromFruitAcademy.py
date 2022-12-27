import requests
from pyquery import PyQuery as pq
import json
import codecs


import DataFromWeb as webData



class FoodsdictionaryRecipe:
    def __init__(self, nameFile):
        self.linksInfo = webData.getDataFromJyson(nameFile)
        if (self.linksInfo == None):
            self.linksInfo = self.makeData(nameFile)

    def get_f(self):
        return self.linksInfo

    def __str__(self):
        return f"{self.linksInfo}"

    def makeData(self, nameFile):
        a=0

        return a


'''
response = requests.get('https://www.foodsdictionary.co.il/articles/875')
html = pq(response.text)
#get the data of the fruits.
table = html.find("table")

myTable = webData.getClassObject(table, "nv-table")
#td= myTable.find("tbody").find("tr").find("td")
print(table)
'''

#dataRecipe= FoodsdictionaryRecipe("jsonFiles/foodsdictionary_recipe.json")

#print(dataRecipe)

# get html from website.
response = requests.get('https://www.foodsdictionary.co.il/Recipes/Types/24#:~:text=%D7%A0%D7%99%D7%AA%D7%9F%20%D7%9C%D7%A2%D7%A9%D7%95%D7%AA%20%D7%A9%D7%99%D7%9E%D7%95%D7%A9%20%D7%91%D7%A4%D7%99%D7%A8%D7%95%D7%AA%20%D7%91%D7%9E%D7%92%D7%95%D7%95%D7%9F%20%D7%9E%D7%AA%D7%9B%D7%95%D7%A0%D7%99%D7%9D%20%D7%9B%D7%9E%D7%95%20%D7%9C%D7%93%D7%95%D7%92%D7%9E%D7%90,%D7%A2%D7%95%D7%A3%20%D7%91%D7%A8%D7%95%D7%98%D7%91%20%D7%99%D7%99%D7%9F%20%D7%95%D7%90%D7%92%D7%A1%D7%99%D7%9D%2C%20%D7%A8%D7%99%D7%91%D7%95%D7%AA%20%D7%91%D7%98%D7%A2%D7%9E%D7%99%D7%9D%20%D7%A9%D7%95%D7%A0%D7%99%D7%9D%20%D7%95%D7%A2%D7%95%D7%93.')
html = pq(response.text)
# get the data of the recipe.
divs = html.find("div")

myTable = webData.getManyClassesObject(divs, "col-limit")
print(myTable)
l=[]
for i in range(len(myTable)):
    l+= webData.getDataAsList(myTable[i], '')
    l[i]['name']= myTable[0].find("h4").text()
print(l)

#ul = myTable.find("tbody").find("tr").find("td").find("ul")

#links = webData.getDataAsList(ul, '')
#webData.saveDataAsJson(nameFile, links)

#webData.enrichData()




