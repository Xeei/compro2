def func(*args):
    print(args, len(args))

func(1,2,3,4,)

def func2(**kwags):
    print(kwags)

func2(a=1, b=2)