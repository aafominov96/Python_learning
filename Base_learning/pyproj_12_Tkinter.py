import tkinter as tk
from tkinter import ttk
import webbrowser as web
from tkinter import *

def clkBtn():
    search()
    pass
def entBtn(event):
    search()
    pass
def search():
    f = text_fill.get()
    check = search_eng.get()
    if f.strip() != "" and f != '    #INPUT SEARCH':
        if check == 'y':
            web.open("https://yandex.ru/search/?lr=213&text=" + f)
        elif check == 'g':
            web.open("https://www.google.com/search?q=" + f)
    else:
        text_fill.delete(0, END)
        text_fill.insert(0, '    #INPUT SEARCH')
    pass


# Создание приложения

app = tk.Tk()
app.title("iFinder")
# app.configure(background='gray')
# Текстовое поле
#search_label = ttk.Label(app, text="Поиск", font='verdana', foreground='blue')
#search_label.grid(row=0, column=0)

# Поле запроса
text_fill = ttk.Entry(app, width=50, text="Hi")
text_fill.grid(row=0, column=1)
text_fill.bind('<Return>', entBtn)

# Кнопка
search_button = ttk.Button(app, text="Search", command=clkBtn)
search_button.grid(row=0, column=2)

search_eng = StringVar()
search_eng.set("g")
# Выбор поисковика
rad_google = ttk.Radiobutton(app, text='Google', value="g", variable=search_eng)
rad_ya = ttk.Radiobutton(app, text='Yandex', value="y", variable=search_eng)
rad_google.grid(row=1, column=1, sticky=W)
rad_ya.grid(row=1, column=1, sticky=E)
# Свойства и параметры
app.wm_attributes('-topmost', True)
text_fill.focus()
app.mainloop()
