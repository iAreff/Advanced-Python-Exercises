
class Course:
    def __init__(self, title, start_date, end_date, level, teacher):
        self._title = title
        self.__start_date = start_date
        self.__end_date = end_date
        self._level = level
        self._teacher = teacher
        self._days_of_week = []

    def add_day(self, day):
        return self._days_of_week.append(day)


class Java(Course):
    def __init__(self, title, start_date, end_date, level, teacher, id, price):
        super().__init__(title, start_date, end_date, level, teacher)
        self.__id = id
        self.__price = price
        
    def __str__(self):
        return f'Course ID: {self.__id}\nCourse Title: {self._title}\nCourse Level: {self._level}\nTeacher: {self._teacher}\nPrice: {self.__price}\nHolding Days: {self._days_of_week}'


class Php(Course):
    def __init__(self, title, start_date, end_date, level, teacher, id, price):
        super().__init__(title, start_date, end_date, level, teacher)
        self.__id = id
        self.__price = price
    
    def __str__(self):
        return f'Course ID: {self.__id}\nCourse Title: {self._title}\nCourse Level: {self._level}\nTeacher: {self._teacher}\nPrice: {self.__price}\nHolding Days: {self._days_of_week}'


class Python(Course):
    def __init__(self, title, start_date, end_date, level, teacher, id, price):
        super().__init__(title, start_date, end_date, level, teacher)
        self.__id = id
        self.__price = price
        
    def __str__(self):
        return f'Course ID: {self.__id}\nCourse Title: {self._title}\nCourse Level: {self._level}\nTeacher: {self._teacher}\nPrice: {self.__price}\nHolding Days: {self._days_of_week}'


#---------------------------------------------------------------------

courses=[]

basic_java = Java('دوره مقدماتی جاوا', '1402/02/01','1402/03/31','A','استاد عارفی پور',101,450000)
basic_java.add_day('شنبه')
basic_java.add_day('چهارشنبه')
courses.append(basic_java)


advanced_java = Java('دوره پیشرفته جاوا', '1402/01/01','1402/06/31','B','استاد جعفری',102,2500000)
advanced_java.add_day('یکشنبه')
advanced_java.add_day('سه‌شنبه')
courses.append(advanced_java)


basic_php = Php('دوره مقدماتی PHP', '1402/03/01','1402/04/31','A','استاد محمدی',103,500000)
basic_php.add_day('دوشنبه')
basic_php.add_day('پنجشنبه')
courses.append(basic_php)


advanced_php = Php('دوره پیشرفته PHP', '1402/02/01','1402/06/31','B','استاد عباسی',104,6500000)
advanced_php.add_day('پنجشنبه')
advanced_php.add_day('جمعه')
courses.append(advanced_php)


basic_python = Python('دوره مقدماتی پایتون', '1402/01/01','1402/02/31','A','استاد نعمتی',105,300000)
basic_python.add_day('شنبه')
basic_python.add_day('یکشنبه')
courses.append(basic_python)


advanced_python = Python('دوره پیشرفته پایتون', '1402/40/01','1402/07/30','B','استاد یزدانی',106,3400000)
advanced_python.add_day('سه‌شنبه')
advanced_python.add_day('چهارشنبه')
courses.append(advanced_python)


for i in courses:
    print(i,end='\n\n')