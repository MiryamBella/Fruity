import requests
from pyquery import PyQuery as pq
import json
import codecs
import DataFromWeb as webData


# get html from website.
response = requests.get('https://www.foodsdictionary.co.il/articles/875')
html = pq(response.text)
# get the data of the fruits.
table = html.find("table")

myTable = webData.getClassObject(table, "textTable")
ul = myTable.find("tbody").find("tr").find("td").find("ul")
links = webData.getDataAsList(ul, '')
for i in range(len(links)):
    response = requests.get(links[i]["link"])
    html = pq(response.text)
    table = html.find("div").find("table")
    myTable = webData.getClassObject(table, "nv-table")
    links[i]["Details"] = (myTable.text()).replace("\nלמה לבדוק ערך תזונתי של מוצר אחד?5 ימי ניסיון חינם במחשבון הקלוריות", '')

    divs = html.find("div")
    clasCenter = webData.getManyClassesObject(divs, "text-center")[2]

    col12 = webData.getManyClassesObject(clasCenter.find("div"), "col-12")
    links[i]["info"]= col12[0].find("p").text()[:-22]










#save
'''
webData.saveDataAsJson(nameFile, links)
'''
















