import requests
from pyquery import PyQuery as pq
import DAL.web_data.DataFromWeb as webData


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
class Foodsdictionary_data:
    def __init__(self, nameFile):
        self.nameFile = nameFile
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

        for i in range(len(links)):
            response = requests.get(links[i]["link"])
            html = pq(response.text)
            table = html.find("div").find("table")
            myTable = webData.getClassObject(table, "nv-table")
            links[i]["Details"] = (myTable.text()).replace(
                "\nלמה לבדוק ערך תזונתי של מוצר אחד?5 ימי ניסיון חינם במחשבון הקלוריות", '')

            divs = html.find("div")
            clasCenter = webData.getManyClassesObject(divs, "text-center")[2]

            col12 = webData.getManyClassesObject(clasCenter.find("div"), "col-12")
            links[i]["info"] = col12[0].find("p").text()[:-22]

        webData.saveDataAsJson(nameFile, links)
        return links

    def GetData_ByName(self, name):
        listinfo=[]
        for f in self.linksInfo:
            if (name in f["name"]):
                listinfo.append(f)

        return listinfo

    def orderData(self):
        for j in range(len(self.linksInfo)):
            splited = self.linksInfo[j]["Details"].split('\n')
            for i in range(0, len(splited), 2):
                splited[i] = splited[i] + ' ' + splited[i + 1]
                splited[i + 1] = None

            while (None in splited):
                splited.remove(None)

            for i in range(len(splited)):
                if ("" in splited[i] and i > 0):
                    splited[i] = splited[i].split("")
                    splited[i - 1] += ' ' + splited[i][0] + " (" + splited[i][1] + ")"
                    splited[i] = None

            while (None in splited):
                splited.remove(None)

            self.linksInfo[j]["Details"] = None
            self.linksInfo[j]["Details"] = []

            for i in range(len(splited)):
                self.linksInfo[j]["Details"].append(splited[i])
        webData.saveDataAsJson(self.nameFile, self.linksInfo)




'''
dataFood= Foodsdictionary_data("jsonFiles/foodsdictionary_info.json")
dataFood.orderData()
data = dataFood.get_f()
for i in data[0]["Details"]:
    print(i)

print("link:", data[1]["link"])

splited=data[1]["Details"].split('\n')
for i in range(0, len(splited), 2):
    splited[i] = splited[i] +' ' + splited[i+1]
    splited[i+1] = None

while (None in splited):
    splited.remove(None)

for i in range(len(splited)):
    if ("" in splited[i] and i>0):
        splited[i] = splited[i].split("")
        splited[i-1] += ' ' + splited[i][0] + " (" + splited[i][1] + ")"
        splited[i] = None

while (None in splited):
        splited.remove(None)

for i in splited:
    print(i)


response = requests.get('https://www.foodsdictionary.co.il/articles/875')
html = pq(response.text)
#get the data of the fruits.
table = html.find("table")

myTable = webData.getClassObject(table, "nv-table")
#td= myTable.find("tbody").find("tr").find("td")
print(table)

#print(getData(links[0]['link'], "col-12"))
#print(webData.enrichData(fruits[22]))

#getText()ְ

webData.saveDataAsJson("fruitsList.json", fruits)
#webData.saveDataAstext("fruitsList.txt", fruits)
#print(fruits)

webData.getDataFromJyson("fruitsList.json")
'''
