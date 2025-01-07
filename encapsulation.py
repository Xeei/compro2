def myprint(c, n):
    try:
        attr_or_method = getattr(c, n)
        print(attr_or_method)
    except AttributeError as e:
        print("***Error:", e)

class MyClassScope1:
    def __init__(self, value):
        self.p1 = f"{self.__class__.__name__} Public ({value})"
        self._p2 = f"{self.__class__.__name__} Protected ({value})"
        self.__p3 = f"{self.__class__.__name__} Private ({value})"

class MyClassScope2(MyClassScope1):
    def __init__(self, value):
        super().__init__("["+value+"]")
        self.p4 = f"{self.__class__.__name__} Public ({value})"
        self._p5 = f"{self.__class__.__name__} Protected ({value})"
        self.__p6 = f"{self.__class__.__name__} Private ({value})"

class MyClassScope3(MyClassScope2):
    def __init__(self, value):
        super().__init__("["+value+"]")
        self.p7 = f"{self.__class__.__name__} Public ({value})"
        self._p8 = f"{self.__class__.__name__} Protected ({value})"
        self.__p9 = f"{self.__class__.__name__} Private ({value})"


print("-" * 20)

# tmp = MyClassScope1("111")
# myprint(tmp, "p1")       # Accessing public attribute
# myprint(tmp, "_p2")      # Accessing protected attribute using myprint function
# myprint(tmp, "__p3")     # Trying to access private attribute using myprint function (will fail)



# print("-" * 20)

# tmp = MyClassScope2("222")
# myprint(tmp, "p1")       # Accessing public attribute
# myprint(tmp, "_p2")      # Accessing protected attribute directly
# myprint(tmp, "__p3")     # Trying to access private attribute using myprint function (will fail)
# myprint(tmp, "p4")       # Accessing public attribute of subclass
# myprint(tmp, "_p5")      # Accessing protected attribute directly
# myprint(tmp, "__p6")     # Trying to access private attribute using myprint function (will fail)

# print("-" * 20)

tmp = MyClassScope3("333")
myprint(tmp, "p1")       # Accessing public attribute
myprint(tmp, "_p2")      # Accessing protected attribute directly
myprint(tmp, "__p3")     # Trying to access private attribute using myprint function (will fail)
myprint(tmp, "p4")       # Accessing public attribute of subclass
myprint(tmp, "_p5")      # Accessing protected attribute directly
myprint(tmp, "__p6")     # Trying to access private attribute using myprint function (will fail)
myprint(tmp, "p7")       # Accessing public attribute of subclass
myprint(tmp, "_p8")      # Accessing protected attribute directly
myprint(tmp, "__p9")     # Trying to access private attribute using myprint function (will fail)

# print("-" * 20)

