from random import randint


class Student:
    __school_name = 'Sardar Soleymani'

    def __init__(self, name, family, grade):
        self.__id = randint(1000,9999)
        self.__name = name
        self.__family = family
        self.__grade = grade

    def __str__(self):
        return f'{self.__name} {self.__family}'

    def __eq__(self, obj):
        if not isinstance(obj, Student):
            return False
        return self.__id == obj.__id and self.__name == obj.__name and self.__family == obj.__family

    def __hash__(self):
        return hash(self.__id)**2 + hash(self.__family)*3 + hash(self.__name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, new_family):
        self.__family = new_family

    def show_information(self):
        return f'Student ID: {self.__id}\nStudent Name: {self.__name}\nStudent Family: {self.__family}\nStudent Grade: {self.__grade}'

    @staticmethod
    def show_courses(n):
        match n:
            case 1:
                print(f'Bekhanim Benevisim Riazi Olum Tarikh')
            case 2:
                print(f'Dikte Riazi Farsi Olum')
            case 3:
                print(f'Riazi Farsi Ensha Tarikh')
            case 4:
                print(f'Joghrafi Riazi Olum Tarikh')
            case 5:
                print(f'Vazrzesh Farsi Farsi Ejtemaei')
            case 6:
                print(f'Tarikh Ensha Dikte Parvareshi')
            case _:
                print('Wrong Grade Number!')

    @classmethod
    def change_shool_name(cls, new_school_name):
        cls.__school_name = new_school_name


# ----------------------------------------------------------
first_names = ["علیرضا", "محمدرضا", "فاطمه", "سارا","حسین", "نگین", "زهرا", "مهدیه","امیرحسین", "محمدجواد"]
last_names = ["محمدی", "احمدی", "علیزاده", "محمدیان","رضایی", "محمدی‌نیا", "صادقی", "رحمانی","موسوی", "حسینی"]
students_list = {Student(first_names[i-1],last_names[i-1],randint(1,6)) for i in range(1,11)}
for i in students_list:
    print(i.show_information())
    print('--------------------------')
    
Student.change_shool_name('Shahid Soleymani')
Student.show_courses(4)


