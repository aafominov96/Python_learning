def summator (a,i=1):
    res = 0
    i_count = 0
    while i_count<i:
        res = res + a**a
        i_count+=1
    return res
test = summator(1,10)
print("Result of summ: ", test)

def script_1(hello):
    Hello = str(hello) + ", "
    def script_2(name):
        return Hello+str(name)
    return script_2
first_1 = "Hello"
second_1 = "Artyom"
second_2 = "Sergey"
second_3 = "Leonid"
namer = script_1(first_1)
print(namer(second_1))
print(namer(second_2))
first_2 = "Hi"
namer = script_1(first_2)(second_3)
print(namer)
del(namer)
namer = lambda hello = "Hi", name = "Joe": hello + ", " +name
print(namer())
