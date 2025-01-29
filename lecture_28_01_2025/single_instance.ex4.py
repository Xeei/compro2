class Parent:
    def __init__(self):
        pass

class MySinglenton(Parent):
    def __new__(cls):
        print("new")
        return super().__new__(cls)

    def __init__(self):
        print("init")


tmp1 = MySinglenton()

print(type(tmp1))
print(isinstance(tmp1, MySinglenton))
print(isinstance(tmp1, Parent)) # True because it also check Parent class
print(isinstance(tmp1, int))