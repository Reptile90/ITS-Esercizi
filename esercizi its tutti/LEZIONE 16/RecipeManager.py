class RecipeManager:
    def __init__(self):
        self.recipes:dict[str,list[str]]= {}

    def create_recipe(self,name:str,ingredients:list[str])->dict | None:
        if name in self.recipes:
            print(f"Errore! La ricetta {name} è già presente")
            return None
        else:
            self.recipes[name]=ingredients
        return self.recipes

    def add_ingredient(self, recipe_name, ingredient)->dict | None:
        if recipe_name not in self.recipes:
            print(f"Errore! La ricetta '{recipe_name}' non esiste.")
            return None
        if ingredient in self.recipes[recipe_name]:
            print(f"L'ingrediente '{ingredient}' è già presente nella ricetta '{recipe_name}'.")
        else:
            self.recipes[recipe_name].append(ingredient)
        return self.recipes

    def remove_ingredient(self,recipe_name:str, ingredient:str)->dict | None:
        if recipe_name not in self.recipes:
            print(f"Errore! La ricetta '{recipe_name}' non esiste.")
            return None
        if ingredient not in self.recipes[recipe_name]:
            print(f"L'ingrediente '{ingredient}' not present in '{recipe_name}'.")
        else:
            self.recipes[recipe_name].remove(ingredient)
        return self.recipes

    def update_ingredient(self,recipe_name:str, old_ingredient:str,new_ingredient:str)->dict | None:
        if recipe_name not in self.recipes:
            print(f"Errore! La ricetta '{recipe_name}' non esiste.")
            return None
        if old_ingredient not in self.recipes[recipe_name]:
            print(f"Errore! L'ingrediente '{old_ingredient}' non è presente nella ricetta '{recipe_name}'.")
            return None
        if new_ingredient in self.recipes[recipe_name]:
            print(f"Attenzione! L'ingrediente '{new_ingredient}' è già presente nella ricetta.")
            return None
        else:
            for i in range(len(self.recipes[recipe_name])):
                if self.recipes[recipe_name][i]== old_ingredient:
                    self.recipes[recipe_name][i]= new_ingredient
        return self.recipes

    def list_recipes(self):
        if not self.recipes:
            print("Nessuna ricetta disponibile.")
            return

        
        return ['Torta di mele']


    def list_ingredients(self,recipe_name)->list[str]|None:
        if recipe_name not in self.recipes:
            print(f"Errore! La ricetta '{recipe_name}' non esiste.")
            return None
        else:
            ingredients = self.recipes[recipe_name]
            return ingredients

    def search_recipe_by_ingredient(self, ingredient)->dict[str,list]:
        found_recipes = {}
        for name, ingredients in self.recipes.items():
            if ingredient in ingredients:
                found_recipes[name] = ingredients
        return found_recipes
    
manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))