
shoppingList1 = ["Milk","Cheese","Butter","Tomato","Banana","Apple"] 
shoppingList2 = ["Orange","Cheese","Kiwi","Tomato","Banana","Butter"]

print(list(filter(lambda x:x, map(lambda x,y: x if x==y else False, shoppingList1,shoppingList2))))
# filter(lambda x: x or False)      other interesting way to write this kind of filter