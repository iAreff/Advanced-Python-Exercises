
class Counter:
    def __init__(self, start, end,increment):
        self.__start = start
        self.__end = end
        self.__increment = increment

    def __iter__(self):
        return self

    def __next__(self):
        self.__start += self.__increment
        if self.__start > self.__end:
            raise StopIteration
        return self.__start


counter = Counter(10, 100, 3)
for i in counter:
    print(i)