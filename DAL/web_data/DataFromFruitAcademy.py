import DAL.web_data.DataFromWeb as webData



class FoodsdictionaryRecipe:
    def __init__(self, nameFile):
        self.recipes = webData.getDataFromJyson(nameFile)
        if (self.recipes == None):
            self.recipes = self.makeData(nameFile)

    def __str__(self):
        return f"{self.recipes}"

    def getRecipes(self):
        return self.recipes

    def makeData(self, nameFile):
        link = 'https://www.foodsdictionary.co.il/Recipes/Types/24#:~:text=%D7%A0%D7%99%D7%AA%D7%9F%20%D7%9C%D7%A2%D7%A9%D7%95%D7%AA%20%D7%A9%D7%99%D7%9E%D7%95%D7%A9%20%D7%91%D7%A4%D7%99%D7%A8%D7%95%D7%AA%20%D7%91%D7%9E%D7%92%D7%95%D7%95%D7%9F%20%D7%9E%D7%AA%D7%9B%D7%95%D7%A0%D7%99%D7%9D%20%D7%9B%D7%9E%D7%95%20%D7%9C%D7%93%D7%95%D7%92%D7%9E%D7%90,%D7%A2%D7%95%D7%A3%20%D7%91%D7%A8%D7%95%D7%98%D7%91%20%D7%99%D7%99%D7%9F%20%D7%95%D7%90%D7%92%D7%A1%D7%99%D7%9D%2C%20%D7%A8%D7%99%D7%91%D7%95%D7%AA%20%D7%91%D7%98%D7%A2%D7%9E%D7%99%D7%9D%20%D7%A9%D7%95%D7%A0%D7%99%D7%9D%20%D7%95%D7%A2%D7%95%D7%93.'
        divs = webData.getDivs(link)
        myTable = webData.getManyClassesObject(divs, "col-limit")
        #create the list and get the names and links.
        listRecipes = []
        for i in range(len(myTable)):
            listRecipes += webData.getDataAsList(myTable[i], 'https://www.foodsdictionary.co.il/')
            listRecipes[i]['name'] = myTable[0].find("h4").text()
        #get the recipes.
        for i in range(len(listRecipes)):
            divs = webData.getDivs(listRecipes[i]['link'])
            cols = webData.getManyClassesObject(divs, "col-lg-12")
            ps = cols[2].find('p')
            p = ps.eq(0)
            listRecipes[i]['info'] = p.text()
            li = webData.getManyClassesObject(divs.find("li"), "list-group-item")
            components = []
            for com in range(1, len(li)):
                components.append(li[com].text())
            recipeOrder = {}
            recipeOrder['components'] = components
            # to get details:
            divs = webData.getDivs(listRecipes[i]['link'])
            details=webData.getClassObject(divs.find("ul"), "recipe-basic-details")
            recipeOrder['Details']= details.text()

            ul = webData.getClassObject(divs.find("ul"), "howto-list")
            recipeOrder['order'] = ul.text()
            listRecipes[i]['recipe'] = recipeOrder
        webData.saveDataAsJson(nameFile, listRecipes)
        return listRecipes

    def getRecipe_byIndex(self, index):
        return self.recipes[index]

    def getRecipe_byname(self, name):
        for r in self.recipes:
            if(name in r['name']):
                return r
        return None

    def getRecipe_byNameComponet(self, com):
        l_recipients=[]
        for r in self.recipes:
            for c in r['recipe']['components']:
                if(com in c):
                    l_recipients.append(r)
        return l_recipients
    def getRecipe_order_byIndex(self, index):
        return self.recipes[index]['recipe']['order']

    def getRecipe_order_byname(self, name):
        for r in self.recipes:
            if(name in r['name']):
                return r['recipe']['order']
        return None

    def delDuplycates(self, nameFile):
        newData=[]
        names= []
        for recipie in self.recipes:
            if(recipie["name"] not in names):
                names.append(recipie["name"])
                newData.append(recipie)
        self.recipes.clear()
        for r in newData:
            self.recipes.append(r)

'''
foodRecipes =FoodsdictionaryRecipe("jsonFiles/fruitAcademy_recipe.json")
foodRecipes.delDuplycates("jsonFiles/fruitAcademy_recipe.json")
for i in foodRecipes.getRecipes():
    print(i)
data=foodRecipes.getRecipes()

for d in data:
    if("ברוק" in d["name"]):
        print(d)

r= foodRecipes.getRecipe_byNameComponet("תמר")
print(data)
#print(r["info"])
#print(foodRecipes.getRecipe_byNameComponet("תמר"))

for i in r["recipe"]["components"]:
    if("תמר" in i):
        print(i)
        print()

#print("order", r["recipe"]["order"])



'''