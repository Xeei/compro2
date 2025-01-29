
class MySinglenton():

    _instance = None

    def __new__(cls, v):
        if cls._instance == None:
            print("new")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, v=None):
        if v is not None:
            self.data = v
            print("init")


tmp1 = MySinglenton("hi")

print(type(tmp1))
print(id(tmp1))
print(tmp1.data)

tmp2 = MySinglenton("testtesttse")

print(type(tmp2))
print(id(tmp2))
print(tmp2.data)