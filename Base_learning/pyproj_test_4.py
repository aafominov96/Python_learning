from tkinter import ttk
from tkinter import *
def grab():
    a = field_1.get()
    try:
        a = float(a)
    except:
        a = 0
    field_1.delete(0, END)
    field_1.focus()
    return a
def plus():
    if field_2.get() == "":
        a = grab()
        field_2.insert(0, str(a)+"+")
    else:
        field_2.delete(0,END)
    pass
def minus():
    if field_2.get() == "":
        a = grab()
        field_2.insert(0, str(a) + "-")
    else:
        field_2.delete(0, END)
    pass
def umn():
    if field_2.get() == "":
        a = grab()
        field_2.insert(0, str(a) + "*")
    else:
        field_2.delete(0, END)
    pass
def delen():
    if field_2.get() == "":
        a = grab()
        field_2.insert(0, str(a) + "/")
    else:
        field_2.delete(0, END)
    pass
def res():
    a = grab()
    res = field_2.get()
    first_num = str()
    i = 0
    try:
        while res[i] != '+' or res[i] != '-' or res[i] != '*' or res[i] != '/':
            if i == len(res)-1:
                break
            else:
                i += 1
            first_num += res[i - 1]
        if res[i] == '+':
            answer = float(first_num) + a
            field_2.insert(END, str(a) + '=' + str(answer))
        elif res[i] == '-':
            answer = float(first_num) - a
            field_2.insert(END, str(a) + '=' + str(answer))
        elif res[i] == '*':
            answer = float(first_num) * a
            field_2.insert(END, str(a) + '=' + str(answer))
        elif res[i] == '/':
            answer = float(first_num) / a
            field_2.insert(END, str(a) + '=' + str(answer))
    except:
        field_2.insert(END, "ERROR")
def clear_all():
    field_1.delete(0, END)
    field_2.delete(0, END)
but_width = 8
app = Tk()
app.title("Калькулятор")
text_1 = ttk.Label(app, text="Введите число:")
text_1.grid(row=0, column=0)
field_1 = ttk.Entry(app)
field_1.grid(row=1, column=0)
text_2 = ttk.Label(app, text="Результат")
text_2.grid(row=0, column=1)
field_2 = ttk.Entry(app)
field_2.grid(row=1, column=1)
btn_plus = ttk.Button(app, width=but_width, command=plus, text="+")
btn_minus = ttk.Button(app, width=but_width, command=minus, text="-")
btn_umn = ttk.Button(app, width=but_width, command=umn, text="*")
btn_delen = ttk.Button(app, width=but_width, command=delen, text="/")
btn_res = ttk.Button(app, width=2*but_width, command=res, text="=")
btn_clear = ttk.Button(app, width=2*but_width, command=clear_all, text='Clear')
btn_clear.grid(row=3, column=1)
btn_res.grid(row=4, column=0)
btn_plus.grid(row=2, column=0, sticky=E)
btn_minus.grid(row=2, column=0, sticky=W)
btn_umn.grid(row=3, column=0, sticky=E)
btn_delen.grid(row=3, column=0, sticky=W)
app.mainloop()