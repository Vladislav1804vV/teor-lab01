# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, messagebox
from math import factorial
from PIL import Image, ImageTk
import time


# =====================================================================================================

# =====================================================================================================

# form_P = "Используется формула перестановок с повторением\n ~P_n^m = n!/(m_1!*m_2!*..*m_k!)"
# Перестановка с повторением
def permutations_with_repeat(n, m_tuple):
    result = factorial(int(n))
    for i in m_tuple:
        result //= factorial(int(i))
    return result


# form_A = "Используется формула размещений с повторением\n ~A_n^m = n^m"
# Размещение с повторением
def accommodation_with_repeat(n, m):
    return int(n) ** int(m)


# form_C = "Используется формула сочетаний без повторения\n С_n^m = n!/( m!*(n-m)!)"
# Сочетание без повторений
def combination_wo_repeat(n, m):
    result = factorial(int(n))
    delitel = factorial(int(m)) * factorial(int(n - m))
    result //= delitel
    return result


# =====================================================================================================

def load_image(name):
    img = Image.open(name)
    return ImageTk.PhotoImage(img)


def set_default_widget():
    A_pic.place_forget()
    P_pic.place_forget()
    C_pic.place_forget()
    txt.delete(0, END)
    result.delete(0, END)
    result.insert(0, "0")
    inputN.delete(0, END)
    inputN.insert(0, 0)
    inputK.delete(0, END)
    inputK.insert(0, 0)


def change_input_data(obj):

    set_default_widget()
    curr = cb_selectformul.get()
    if curr == "Сочетание без повторения":
        inputK.configure(state="normal")
        txt.configure(state="disabled")
        C_pic.place(x=500, y=30)
    if curr == "Размещение с повторением":
        inputK.configure(state="normal")
        txt.configure(state="disabled")
        A_pic.place(x=500, y=30)
    if curr == "Перестановки с повторением":
        inputK.configure(state="disabled")
        txt.configure(state="normal")
        P_pic.place(x=500, y=30)


def check_subsets(tuple):
    sum = 0
    for i in tuple:
        if int(i) < 0:
            messagebox.showerror('Ошибка', 'Неправильные данные, введены отрицательные значения')
            return -1
        sum += int(i)
    return sum == int(inputN.get())


def calc_result():
    result.delete(0, END)

    if int(inputN.get()) < 0 or int(inputK.get())<0:
        messagebox.showerror('Ошибка', 'Неправильные данные, введены отрицательные значения')
    elif inputN.get() < inputK.get():
        messagebox.showerror('Ошибка', 'Неправильные данные, должно соблюдаться условие N >= K')
    else:
        curr = cb_selectformul.get()
        if curr == "Сочетание без повторения":
            result.insert(0, combination_wo_repeat(int(inputN.get()), int(inputK.get())))
        if curr == "Размещение с повторением":
            result.insert(0, accommodation_with_repeat(int(inputN.get()), int(inputK.get())))
        if curr == "Перестановки с повторением":
            tuple = txt.get()
            tuple = tuple.split(",")
            check = check_subsets(tuple)
            if check == 1:
                result.insert(0, permutations_with_repeat(int(inputN.get()), tuple))
            elif check == 0:
                messagebox.showerror('Ошибка', 'Неправильные данные, должно соблюдаться условие \n n = n1+n2+..n_k')


# Создание окна
window = Tk()
window.title("Lab01")
window.geometry('1200x400')

# Загрузка изображений
A = load_image("accommodation.png")
C = load_image("combination.png")
P = load_image("permutations.png")

# Создание изображений в окне
A_pic = Label(window, image=A, anchor=NW)
A_pic.image = A
A_pic.place(x=500, y=30)

P_pic = Label(window, image=P, anchor=NW)
P_pic.image = P

C_pic = Label(window, image=C, anchor=NW)
C_pic.image = C

# Размещение элементов в окне
label_form = Label(window,
                   text="Выберите формулу")
label_form.place(x=10, y=10)

cb_selectformul = ttk.Combobox(window,
                               values=[
                                   "Сочетание без повторения",
                                   "Размещение с повторением",
                                   "Перестановки с повторением"], width=35, state="readonly")
cb_selectformul.place(x=14, y=40)
cb_selectformul.current(0)

label_form1 = Label(window,
                    text="Введите n")
label_form1.place(x=10, y=80)

inputN = Spinbox(window, from_=0, to=10000, width=5)
inputN.place(x=14, y=110)

label_form2 = Label(window,
                    text="Введите k ")
label_form2.place(x=150, y=80)

inputK = Spinbox(window, from_=0, to=10000, width=5)
inputK.place(x=154, y=110)

label_form2 = Label(window,
                    text="Введите подмножество повторяющихся элементов ")
label_form2.place(x=10, y=150)

txt = Entry(window, width=30)
txt.place(x=14, y=180)

label_form3 = Label(window,
                    text="Результат ")
label_form3.place(x=10, y=260)

result = Entry(window, width=150)
result.place(x=10, y=290)

btn_result = Button(window, text="Посчитать", command=calc_result)
btn_result.place(x=10, y=220)

change_input_data(None)

cb_selectformul.bind("<<ComboboxSelected>>", change_input_data)
window.mainloop()
