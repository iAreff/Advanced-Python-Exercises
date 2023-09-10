from khayyam import *

class Citizen():
    def __init__(self,name,family,birth_date):
        self.__name = name
        self.__family = family
        self.__birth_date = JalaliDate(*birth_date.split('/'))

    def vaccination_permission(self):
        if self.__birth_date.year < 1340:
            return False
        return True

while True:
    try:
        name , family = input("What's your name: ").split(' ')
        birth_date = input('Enter your birth date: ')
        print(Citizen(name,family,birth_date).vaccination_permission())
    except ValueError as error:
        print(error)
    else:
        print('--------------------------')
        if input('Wanna create other object? (Yes/No) : ').upper() != 'YES':
            break