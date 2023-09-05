from random import randint


class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class PlayerSelection:
    def __init__(self, age, height, weight):
        
        if not age.isdigit() and height.isdigit() and weight.isdigit():
            raise MyException('Enter a number')
        if not 15 <= int(age) <= 35:
            raise MyException('age out of range')
        if not 170 <= int(height) <= 190:
            raise MyException('height out of range')
        if (15 <= int(age) < 25) and not (60 <= int(weight) <= 80):
            raise MyException('weight out of range')
        elif (25 <= int(age) <= 35) and not (50 <= int(weight) <= 75):
            raise MyException('weight out of range')
        
        self.__id = randint(1000,9999)
        self.__age= age
        self.__height = height
        self.__weight = weight
    
    def __str__(self):
        return str(self.__id)
    
#----------------------------------------------------

while True:
    try:
        PlayerSelection(input('How old are you: '),input('How tall are you: '),input('How much do you weigh: '))
    except MyException as error:
        print(error)
    else:
        print('--------------------------')
        if input('Wanna create other object? (Yes/No) : ').upper() != 'YES':
            break