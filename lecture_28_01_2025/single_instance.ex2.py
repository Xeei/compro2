class MySinglenton:

    _instance = None

    def __init__(self):
        if MySinglenton._instance == None:
            self.a = "1"
            MySinglenton._instance = self
        else:
            raise ValueError('Not allow')

    
    @classmethod
    def getInstance(cls):
        return cls._instance
    

tmp = MySinglenton()
print(tmp)
print(id(tmp))
print(tmp.a)
print('='*10)

tmp2 = MySinglenton.getInstance()
print(tmp2)
print(id(tmp2))
print(tmp2.a)
print('='*10)

tmp3 = MySinglenton.getInstance()
print(tmp3)
print(id(tmp3))
print(tmp3.a)
print('='*10)

tmp4 = MySinglenton.getInstance()
print(tmp4)
print(id(tmp4))
print(tmp4.a)
print('='*10)
