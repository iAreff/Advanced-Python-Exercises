
def list_normalizer(func):
    def inner(*args,**kwargs):
        normalized_list = []
        for i in args:
            if not i<0 and type(i)==int:
                normalized_list.append(i)
        return func(*normalized_list)
    return inner


def factorial(n):
        if not n:
            return 1
        return n*factorial(n-1)


@list_normalizer
def list_factorial(*args):
    result_list = []
    for i in args:
        result_list.append(factorial(i))
    return result_list

#--------------------------------------------
numbers_List = [4, 3, 8, 0, -3, -45, 2, 10, -16, 23, 9, 1, -6, 55, 3.4, 6, 11.5]
print(list_factorial(*numbers_List))