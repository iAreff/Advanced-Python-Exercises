import re

with open('Tamrin 9 (Regex - WebScrapping)/information.txt') as file, open('Tamrin 9 (Regex - WebScrapping)/matched_information.csv','w') as output:
    data = file.read()
    found_matches = re.findall(r'Name:\w+,Family:\w+,Mobile:0912\d+,Postal Code:\d+,city:Tehran',data)
    result = 'Name,Family,Mobile,Postal_Code,City\n'
    for i in found_matches:
        result += re.sub(r'Name:(\w+),Family:(\w+),Mobile:(0912\d+),Postal Code:(\d+),city:(Tehran)','\g<1>,\g<2>,\g<3>,\g<4>,\g<5>',i) + '\n'
    output.write(result)