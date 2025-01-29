import random

class MyList():
    def __init__(self, data):
        self.__data = data
        self.__index = 0
        self.__index2 = len(self.__data)-1

    def __iter__(self): # ถ้า for loop จะมาเรียก iter
        return self
    
    def __process(a=None, b=None):
        print("hello")

    @staticmethod
    def __is_prime(n):
        """Check if a number is a prime number."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    # def __next__(self): # การ loop จะเป็นการเรียก next ซ้ำๆ
    #     # return "hello"
    #     if self.__index < len(self.__data):
    #         value = self.__data[self.__index]
    #         value2 = self.__data[self.__index2]
    #         self.__index += 1
    #         self.__index2 -= 1
    #         self.__process()
    #         return (value, value2)
    #     raise StopIteration

    def __next__(self):
        while self.__index < len(self.__data):
            value = self.__data[self.__index]
            self.__index += 1
            if self.__is_prime(value):
                return value
        raise StopIteration

r = [i for i in range(0, 1000000)]
# print(r)
b = MyList(r)
# print(r)

# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

for i in b:
    print(i)
