
customers_list = ["Sara Ahmadi","Ali Rezaee","Bahar Sadr","Ahmad Majedpoor","Iman Mohammadi","Mina Bavandpoor","Mohammad Alimoradi","Majid Rafiee","Sima Sefidiyan"]

special_customers_list = ["Vahid Abdoli","Ali Rezaee","Bahar Sadr","Sima Sefidiyan"] 

print(list(filter(lambda x: x in special_customers_list,customers_list)))