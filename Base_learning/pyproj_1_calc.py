
print("Добро пожаловать в калькулятор: \n")
flag_check = input("Хотите ли Вы что-то посчитать? ")
if flag_check=="Да":
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = input("Выберите действие (+  -  *  /): ")
    res = 0
    if c=="+":
        res = a+b
        print(res)
    elif c=="-":
        res = a-b
        print(res)
    elif c=="*":
        res = a*b
        print(res)
    elif c=="/":
        res = a/b
        print(res)
    else:
        print("Ошибка 404")
else:
    print("Возвращайся скорее!!!")