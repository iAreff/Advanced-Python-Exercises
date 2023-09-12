import json


class FoodMenu:
    def __init__(self,id,food_name,food_price):
        self.id = id
        self.food_name = food_name
        self.food_price = food_price
        self.food_ingredients = []
    
    def add_ingredients(self,*ingredients):
        self.food_ingredients.extend(ingredients)


f1 = FoodMenu(1,'Hamburger',77000)
f1.add_ingredients('Bread','Cheese','Hamburger')

f2 = FoodMenu(2,'Pizza',88000)
f2.add_ingredients('Meat','Cheese','Tomato')

f3 = FoodMenu(3,'Pasta',65000)
f3.add_ingredients('Spaghetti','Sause')

f4 = FoodMenu(4,'Sushi',54000)
f4.add_ingredients('Fish','Vinegar')

food_list = [f1.__dict__,f2.__dict__,f3.__dict__,f4.__dict__]

with open('Tamrin 8 (JSON)/FoodMenu.json','w') as file:
    json.dump(food_list,file,indent=4)