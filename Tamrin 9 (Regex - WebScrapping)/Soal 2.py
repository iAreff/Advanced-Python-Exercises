import requests
import json
from bs4 import BeautifulSoup

source = requests.get('https://www.entekhabcenter.com/product-category/product/audio-video/television')
data = BeautifulSoup(source.content,"html.parser")

name_selector = []
for i in data.select('h5'):
    name_selector.append(i.text)

price_selector = []
for i in data.select('ins'):
    price_selector.append(i.text)

product_list = []
for i in range(len(price_selector)):
    temp = {}
    product_list.append(temp)
    temp['Name'] = name_selector[i]
    temp['Price'] = price_selector[i]


with open('Tamrin 9 (Regex - WebScrapping)/products.json','w',encoding='utf-8') as file:
    json.dump(product_list,file,indent=4,ensure_ascii=False)