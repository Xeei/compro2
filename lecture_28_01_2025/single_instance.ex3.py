class MySinglenton:

    _instance = None

    def __init__(self, value):
        if MySinglenton._instance == None:
            self.a = value
            MySinglenton._instance = self


    
    @classmethod
    def getInstance(cls):
        return cls._instance
    

tmp = MySinglenton(5)
print(tmp)
print(id(tmp))
print(tmp.a)
print('='*10)

tmp2 = MySinglenton.getInstance()
print(tmp2)
print(id(tmp2))
print(tmp2.a)
print('='*10)

tmp3 = MySinglenton(10) # should be error because already have instance
print(tmp3)
print(id(tmp3))
print(tmp3.a)
print('='*10)

tmp4 = MySinglenton.getInstance()
print(tmp4)
print(id(tmp4))
print(tmp4.a)
print('='*10)
