from UI.PaginationApp import PaginationApp


class RecipeByComponent:
    def __init__(self, recipes, component):
        self.recipesIndex = []
        self.mainComponent = component
        num= 0
        for r in recipes:
            for c in r['recipe']['components']:
                if component in c:
                    self.recipesIndex.append(num)
                    break
            num= num +1
        self.pagination = PaginationApp(self.recipesIndex, 5)  # default page size is 5.

    def __str__(self):
        return "Recipes indexes:"+ self.recipesIndex.__str__()+"\nThe main component is: "+ self.mainComponent

    def GetAllRecipintsIndex(self, page_numer, size):
        return self.pagination.goto_page(page_numer, size)

