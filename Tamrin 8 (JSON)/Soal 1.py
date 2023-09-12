import json
import jmespath

with open('Tamrin 8 (JSON)/employee.json') as file:
    data = json.load(file)
    print(jmespath.search("[?gender=='female'].fullName",data))
    print('---------------------')
    print(jmespath.search("[?gender=='male' && company=='MAPNA'].fullName",data))
    print('---------------------')
    print(jmespath.search("[?company=='Iran Khodro Co.'].[fullName, email]",data))
    print('---------------------')
    print(jmespath.search("[?gender=='male'] | sort_by(@, &salary) | reverse(@) | [:3]",data))