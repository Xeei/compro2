class Calculator:

    __rate = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_calculator(cls, rate):
        _rate = rate or cls.__rate
        cls(_rate)

    


