from abc import ABC, abstractmethod
import enum


# class MyException(Exception):
#     def __init__(self, message):
#         super().__init__(message)


class UniversityRanking(enum.Enum):
    rank1 = 100
    rank2 = 80
    rank3 = 60


class Average(enum.Enum):
    top = 100
    excellent = 80
    good = 60


class Participant(ABC):
    def __init__(self, code, name, family, major, address):
        super().__init__()
        self.__code = code
        self.__name = name
        self.__family = family
        self.__major = major
        self.__address = address
        self._final_score = None

    @abstractmethod
    def calculate_score(self):
        pass
    
    def __str__(self):
        return f'ID: {self.__code}\nName: {self.__name}\nFamily: {self.__family}'


class IndependentParticipant(Participant):
    def __init__(self, code, name, family, major, address, exam_score, interview_score):
        super().__init__(code, name, family, major, address)
        
        if exam_score.isdigit() and int(exam_score) <= 100:
            self.__exam_score = exam_score
        else:
            raise ValueError(f'Your entered score ({exam_score}) is wrong!! Please enter a number up to 100')
        
        if interview_score.isdigit() and int(interview_score) <= 100:
            self.__interview_score = interview_score
        else:
            raise ValueError(f'Your entered score ({interview_score}) is wrong!! Please enter a number up to 100')
        

    def calculate_score(self):
        self._final_score = (self.__exam_score + self.__interview_score) / 2
        return self._final_score
    
    def __str__(self):
        return super().__str__()


class EliteGraduate(Participant):
    def __init__(self, code, name, family, major, address, average, university_ranking):
        super().__init__(code, name, family, major, address)
        
        if 16 <= float(average) < 17.5:
            self.__average = Average.good.value
        elif 17.5 <= float(average) < 18.5:
            self.__average = Average.excellent.value
        elif float(average) >= 18.5:
            self.__average = Average.top.value
        else:
            raise ValueError(f'Your entered average ({average}) is wrong!! Please enter a number between 16 and 20')
        
        if university_ranking.isdigit():
            if int(university_ranking) == 1:
                self.__university_ranking = UniversityRanking.rank1.value
            elif 2:
                self.__university_ranking = UniversityRanking.rank2.value
            elif 3:        
                self.__university_ranking = UniversityRanking.rank3.value
            else:
                raise ValueError(f'Wrong Entry! (Enter 1,2 or 3)')
        else:
            raise ValueError(f'Your entered ranking ({university_ranking}) is wrong!! Please enter a number')

    def calculate_score(self):
        self._final_score = (self.__average + self.__university_ranking) / 2
        return self._final_score
    
    def __str__(self):
        return super().__str__()


class ContractEmployee(Participant):
    def __init__(self, code, name, family, major, address, employment_length, performance_score):
        super().__init__(code, name, family, major, address)
        
        if employment_length.isdigit() and int(employment_length) >= 1 and int(employment_length) <= 5:
            self.__employment_length = 0.1
        elif employment_length.isdigit() and int(employment_length) > 5:
            self.__employment_length = 0.2
        else:
            raise ValueError(f'Your entered time ({employment_length}) is wrong!! Please Enter a number (at least 1)')
        
        if performance_score.isdigit() and int(performance_score) <= 100:
            self.__performance_score = performance_score
        else:
            raise ValueError(f'Your entered score ({performance_score}) is wrong!! Please enter a number up to 100')

    def calculate_score(self):
        self._final_score = (self.__employment_length * self.__performance_score) + self.__performance_score
        return self._final_score
    
    def __str__(self):
        return super().__str__()

# ---------------------------------------------------------

def create_object():
    from random import randint
    def get_participant_type():    
        global created_object
        match participant_type:
            case 'A':
                exam_score = input('Enter your exam score: ')
                interview_score = input('Enter your interview score: ')
                created_object = IndependentParticipant(random_code(),name,family,major,address,exam_score,interview_score)
            case 'B':
                average = input('Enter your average: ')
                university_ranking = input('Enter your university ranking: ')
                created_object = EliteGraduate(random_code(),name,family,major,address,average,university_ranking)
            case 'C':
                employment_length = input('Enter your employment length: ')
                performance_score = input('Enter your performance score: ')
                created_object = ContractEmployee(random_code(),name,family,major,address,employment_length,performance_score)
            case _:
                raise ValueError(f'Wrong Entry! ( Enter A,B or C )')
    
    random_code = lambda:randint(10000,99999)
    name = input('Enter your first Name: ')
    family = input('Enter your last Name: ')
    major = input('Whats your major?\nanswer: ')
    address = input('Enter your address: ')
    participant_type = input("What Are You?\nEnter 'A' if you're an independent participant\nEnter 'B' if you're an elite graduate\nEnter 'C' if you're a contract employee\nAnswer: ")
    get_participant_type()
    print(f'Object Created:\n{created_object}')
    return created_object


objects_list = []

while True:
    try:
        objects_list.append(create_object())
    except ValueError as error:
        print(error)
    else:
        print('--------------------------')
        if input('Wanna create other object? (Yes/No) : ').upper() != 'YES':
            break

for i in objects_list:
    print(i)
    print('-----')