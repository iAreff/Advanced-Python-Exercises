class Person:
    def __init__(self, name, family):
        self._name = Person.__normalize_data(name)
        self._family = Person.__normalize_data(family)

    def __str__(self):
        return f'{self._name} {self._family}'

    def __normalize_data(data):
        return data.strip().title()


class Manager(Person):
    managers_count = 0
    managers = []

    def __init__(self, name, family, id, salary):
        super().__init__(name, family)
        self.__id = id
        self.__salary = salary
        Manager.managers_count += 1

    def __str__(self):
        return super().__str__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Employee(Person):
    employees_count = 0
    employees = []

    def __init__(self, name, family, id, rank):
        super().__init__(name, family)
        self.__id = id
        self.__rank = rank
        Employee.employees_count += 1

    def __str__(self):
        return super().__str__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class Trainee(Person):
    trainees_count = 0
    trainees = []

    def __init__(self, name, family):
        super().__init__(name, family)
        self.__training_length = 12
        Trainee.trainees_count += 1

    def __str__(self):
        return super().__str__()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


# -----------------------------------------------------------

manager_1 = Manager('jafar', 'mohseni', 45, 850000)
manager_2 = Manager('milad ', 'abbasi', 89, 2500000)
Manager.managers.append(str(manager_1))
Manager.managers.append(str(manager_2))

employee_1 = Employee('ali  ', 'ahmadi', 23, 'A')
employee_2 = Employee(' farhad', ' malmir', 28, 'C')
Employee.employees.append(str(employee_1))
Employee.employees.append(str(employee_2))

trainee_1 = Trainee('armin   ', 'movahed')
trainee_2 = Trainee('zahra   ', 'shahi')
Trainee.trainees.append(str(trainee_1))
Trainee.trainees.append(str(trainee_2))

print(f'Managers count: {Manager.managers_count}')
print(Manager.managers)
print(f'Employees count: {Employee.employees_count}')
print(Employee.employees)
print(f'Trainees count: {Trainee.trainees_count}')
print(Trainee.trainees)
