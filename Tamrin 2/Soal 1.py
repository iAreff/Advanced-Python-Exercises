class Company:
    def __init__(self, name, manager, address, employee_count, revenue):
        self.__name = name
        self.__manager = manager
        self.__address = address
        self.__employee_count = employee_count
        self.__revenue = revenue

    def __str__(self):
        return f'company name: {self.__name}\nmanager name: {self.__manager}\naddress: {self.__address}'

    def productivity(self):
        return self.__revenue//self.__employee_count


# ------------------------------------------------------------------

xyz = Company('XYZ', 'Aref', 'Karaj', 120, 6500000000)
print(xyz)
print(xyz.productivity())
