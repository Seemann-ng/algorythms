from typing import List


class Recipe:
    def __init__(self, name: str, ingredients: List[str]):
        self.name = name
        self.ingredients = ingredients

    def printIngredients(self):
        print(f"ingredients for {self.name}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"""Today we're cooking {self.name}.\n
              We follow the instructions for preparing the dish {self.name}...\n
              The dish {self.name} is ready.""")


spaghetti = Recipe("Spaghetti Bolognese", ["Spaghetti", "Ground meat", "Tomato sauce", "Onion", "Garlic", "Salt"])
cake = Recipe("Cake", ["Flour", "Eggs", "Milk", "Sugar", "Butter", "Salt", "Vanillin"])

spaghetti.printIngredients()
spaghetti.cook()
cake.printIngredients()
cake.cook()
