class Person:
    def __init__(self, name, family, mobile_number, email):
        from random import randint
        self._temp1 = {}
        self._temp1['ID'] = self.__id = randint(1000,9999)
        self._temp1['Name'] = self.__name = name
        self._temp1['Family'] = self._family = family
        self._temp1['Mobile Number'] = self.__mobile_number = mobile_number
        self._temp1['Email'] = self.__email = email


class Address:
    def __init__(self, city, street, house_number):
        self._temp2 = {}
        self._temp2['City'] = self.__city = city
        self._temp2['Street'] = self.__street = street
        self._temp2['House Number'] = self.__house_number = house_number


class Contact(Person, Address):
    def __init__(self, name, family, mobile_number, email, city, street, house_number):
        Person.__init__(self, name, family, mobile_number, email)
        Address.__init__(self, city, street, house_number)
        self.__information = self._temp1 | self._temp2

    def __str__(self):
        return str(self.__information)


class PhoneBook:
    def __init__(self):
        self.__contacts_list = []

    def __str__(self):
        return str(self.__contacts_list)

    def add_contact(self, contact):
        self.__contacts_list.append(contact)

    def search(self, family):
        for contact in self.__contacts_list:
            if family == contact._family:
                return contact
        return 'Not Found'


# -----------------------------------------------

contact1 = Contact('aref', 'amnollahi', '09357833111',
                   'aref@gmail.com', 'karaj', 'fardis', '99')
contact2 = Contact('ali', 'samadi', '09331564558',
                   'ali@gmail.com', 'qaz', 'valiasr', '35')
contact3 = Contact('mohsen', 'yeganeh', '09126548887',
                   'ziba@gmail.com', 'teh', 'vanak', '15')
phonebook1 = PhoneBook()
phonebook1.add_contact(contact1)
phonebook1.add_contact(contact2)
phonebook1.add_contact(contact3)
# print(phonebook1)
print(phonebook1.search('amnollahi'))
# print(contact1)