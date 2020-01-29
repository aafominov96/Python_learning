def plus(a = 0, b = 0):
    return a+b
def min(a = 0, b = 0):
    return a-b
def umn(a = 0, b = 0):
    return a*b
def delen(a = 0, b = 1):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        result = 0
    return result
def check_fun():
    check = input("Продолжить вычисления? ")
    if check == "Да" or check == "да" or check == "+" or check == "Yes" or check == "yes" or check == "y":
        flag = 1
    else:
        flag = 0
    return flag

if __name__ == '__main__':
    print("Добро пожаловать в вычислитель")
    check = 0
    res = -1
    while (check != 1):
        try:
            rej = int(input("С чем Вы хотите работать? 1 - множества, 0 -числа:  "))
        except ValueError:
            rej = 0
            print("Ошибка ввода: работа с числами в автоматическом режиме")
        if rej == 0:
            if res == -1:
                try:
                    a = float(input("Введите число a: "))
                except ValueError:
                    a = 0
                    print("Ошибка ввода: работа с a = 0")
            else:
                a = res
            try:
                b = float(input("Введите число b: "))
            except ValueError:
                b = 0
                print("Ошибка ввода: работа с b = 0")
            flag = input("Выберите действие: ")
            if flag == "+":
                res = plus(a, b)
                print(a, "+", b, "=", res)
                if check_fun() == 1:
                    check = 0
                    pres = input("Работать с полученным результатом?   ")
                    if pres != "Да" and pres != "да" and pres != "+" and pres != "Yes" and pres != "yes" and pres != "y":
                        res = -1
                else:
                    check = 1
            elif flag == "-":
                res = min(a, b)
                print(a, "-", b, "=", res)
                if check_fun() == 1:
                    check = 0
                    pres = input("Работать с полученным результатом?   ")
                    if pres != "Да" and pres != "да" and pres != "+" and pres != "Yes" and pres != "yes" and pres != "y":
                        res = -1
                else:
                    check = 1
            elif flag == "*":
                res = umn(a, b)
                print(a, "*", b, "=", res)
                if check_fun() == 1:
                    check = 0
                    pres = input("Работать с полученным результатом?   ")
                    if pres != "Да" and pres != "да" and pres != "+" and pres != "Yes" and pres != "yes" and pres != "y":
                        res = -1
                else:
                    check = 1
            elif flag == "/":
                res = delen(a, b)
                print(a, "/", b, "=", res)
                if check_fun() == 1:
                    check = 0
                    pres = input("Работать с полученным результатом?   ")
                    if pres != "Да" and pres != "да" and pres != "+" and pres != "Yes" and pres != "yes" and pres != "y":
                        res = -1
                else:
                    check = 1
            else:
                print("Неверное действие")
                if check_fun() == 1:
                    check = 0
                else:
                    check = 1
        elif rej == 1:
            flag_mnoz_1 = 1
            mn_1 = set()
            while flag_mnoz_1:
                try:
                    a = float(input("Введите число из множества 1:  "))
                except ValueError:
                    a = 0
                    print("Ошибка ввода: 0 в автоматическом режиме")
                mn_1.add(a)
                mn_1_check = input("Добавить число?: +, если да,   -, если нет   ")
                if mn_1_check == "+":
                    flag_mnoz_1 = 1
                else:
                    flag_mnoz_1 = 0
            flag_mnoz_2 = 1
            mn_2 = set()
            while flag_mnoz_2:
                try:
                    a = float(input("Введите число из множества 1:  "))
                except ValueError:
                    a = 0
                    print("Ошибка ввода: 0 в автоматическом режиме")
                mn_2.add(a)
                mn_2_check = input("Добавить число?: +, если да,   -, если нет   ")
                if mn_2_check == "+":
                    flag_mnoz_2 = 1
                else:
                    flag_mnoz_2 = 0
            print("Полученные множества: \n Множество №1: ", mn_1, "\n", "Множество №2: ", mn_2)
            flag = input("Что вы хотите сделать с множествами? \n Пересечение - '*' \n Объединение - '+' \n Вычитание - '-' \n          ")
            if flag == "+":
                mn_1.update(mn_2)
                print("Полученное множество №3", mn_1)
                if check_fun() == 1:
                    check = 0
                else:
                    check = 1
            elif flag == "*":
                mn_1.intersection_update(mn_2)
                print("Полученное множество №3", mn_1)
                if check_fun() == 1:
                    check = 0
                else:
                    check = 1
            elif flag == "-":
                mn_1.difference_update(mn_2)
                print("Полученное множество №3",mn_1 )
                if check_fun() == 1:
                    check = 0
                else:
                    check = 1
            else:
                print("Неверное действие")
                if check_fun() == 1:
                    check = 0
                else:
                    check = 1
