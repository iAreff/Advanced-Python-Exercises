import collections



Smartphone = collections.namedtuple('Samrtphone','brand model price colors')

smartphone1 = Smartphone('Xiaomi','12',24,['black','white'])
smartphone2 = Smartphone('Poco','F3',21,['blue','black','white'])
smartphone3 = Smartphone('Samsung','A53',13,['red'])
smartphone4 = Smartphone('Apple','Iphone 14',8,['gray','pink','white','yellow'])

products_list = [smartphone1,smartphone2,smartphone3,smartphone4]

for i in products_list:
    print(i._asdict())