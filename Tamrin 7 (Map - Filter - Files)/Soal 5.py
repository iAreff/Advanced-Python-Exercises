import os

try:
    myfile_path = 'tamrin 7/myfile.txt'
    description_path = 'tamrin 7/description.txt'
    
    with open(myfile_path) as myfile:
        text = myfile.read().replace('inbuilt','built-in')
    
    with open(myfile_path,'w') as myfile:
        myfile.write(text)
    
    with open(description_path,'w') as description:
        description.write(f"File Name: {os.path.basename('Tamrin 7 (Map - Filter - Files)/myfile.txt')}\nFile Size: {os.path.getsize('tamrin 7/myfile.txt')//1024} KB")

except Exception as error:
    print(error)

finally:
    if myfile:
        myfile.close()
    if description:
        description.close()