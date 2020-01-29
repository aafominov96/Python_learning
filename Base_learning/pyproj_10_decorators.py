def decorator_1(func):
    def decor_in_func():
        print("Hello")
        a = func()
        print("GoodBye")
        return a
    return decor_in_func

@decorator_1
def summator():
    a = input("a = ")
    b = input("b = ")
    s = a+b
    return s

summa = summator()
print(summa)