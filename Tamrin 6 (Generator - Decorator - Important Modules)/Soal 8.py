import collections

class MyString(collections.UserString):
    def reverse(self):
        return self[::-1]
    
    def insert(self,text,index):
        edited_string = list(self.data)
        edited_string[index] = text
        return ''.join(edited_string)


str1 = MyString('Aref Amnollahi')

print(str1.reverse())

print(str1.insert('new word',2))