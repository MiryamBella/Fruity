import DAL.web_data.DataFromWeb as webData


class FoodsdictionaryRecipe:
    def __init__(self, nameFile):
        self.nameFile = nameFile
        self.recipes = webData.getDataFromJyson(nameFile)
        if (self.recipes == None):
            self.recipes = self.makeData(nameFile)

    def __str__(self):
        return f"{self.recipes}"

    def getRecipes(self):
        return self.recipes

    def makeData(self, nameFile):
        listRecipes = []
        runNum=0
        for number in range(9):
            print(number)
            if(number==0):
                link = 'https://www.foodsdictionary.co.il/Recipes/Types/24/'
            else:
                link = 'https://www.foodsdictionary.co.il/Recipes/Types/24/'+ str(number)
            divs = webData.getDivs(link)
            myTable = webData.getManyClassesObject(divs, "col-limit")
            #create the list and get the names and links.
            tempList=[]
            for i in range(len(myTable)):
                tempList += webData.getDataAsList(myTable[i], 'https://www.foodsdictionary.co.il/')
                tempList[i]['name'] = myTable[i].find("h4").text()
            #get the recipes.
            for i in range(len(tempList)):
                divs = webData.getDivs(tempList[i]['link'])
                cols = webData.getManyClassesObject(divs, "col-lg-12")
                ps = cols[2].find('p')
                p = ps.eq(0)
                tempList[i]['info'] = p.text()
                li = webData.getManyClassesObject(divs.find("li"), "list-group-item")
                components = []
                for com in range(1, len(li)):
                    components.append(li[com].text())
                recipeOrder = {}
                recipeOrder['components'] = components
                # to get details:
                divs = webData.getDivs(tempList[i]['link'])
                details=webData.getClassObject(divs.find("ul"), "recipe-basic-details")
                recipeOrder['Details']= details.text()
    
                ul = webData.getClassObject(divs.find("ul"), "howto-list")
                recipeOrder['order'] = ul.text()
                tempList[i]['recipe'] = recipeOrder
                tempList[i]['index'] = runNum
                runNum+=1
            listRecipes+= tempList
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
                    break
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
        webData.saveDataAsJson(nameFile, self.recipes)

    def order_recipients(self):

        for r in range(len(self.recipes)):
            for i in range(len(self.recipes[r]["recipe"]["components"])):
                self.recipes[r]["recipe"]["components"][i] = self.recipes[r]["recipe"]["components"][i].replace("\n",' ')
                if ("" in self.recipes[r]["recipe"]["components"][i]):
                    self.recipes[r]["recipe"]["components"][i] = self.recipes[r]["recipe"]["components"][i].split("")
                    self.recipes[r]["recipe"]["components"][i] = self.recipes[r]["recipe"]["components"][i][0] + " (" + self.recipes[r]["recipe"]["components"][i][1] + ")"
            lengh = (len(self.recipes[r]["recipe"]["components"]) + 1) // 7
            self.recipes[r]["recipe"]["components"] = (self.recipes[r]["recipe"]["components"])[(-lengh):]
        #webData.saveDataAsJson(self.nameFile, self.recipes)


#foodRecipes =FoodsdictionaryRecipe("jsonFiles/fruitAcademy_recipe.json")
#data=foodRecipes.getRecipes()
