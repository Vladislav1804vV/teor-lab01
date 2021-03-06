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


def calc_exer1():
    k = int(K.get())
    l = int(L.get())
    s = int(S_.get())
    r = int(R.get())

    if k < 0 or l < 0 or s < 0 or r < 0:
        messagebox.showerror('Ошибка', 'Неправильные данные, введены отрицательные значения')
    elif l < k and r <= k and s <= l and r-s <= k-l:
        calc = combination_wo_repeat(l, s) * combination_wo_repeat((k - l), (r - s)) / combination_wo_repeat(k, r)
        result2.delete(0, END)
        result2.insert(0, calc)
    else:
        if l >= k:
            messagebox.showerror('Ошибка', 'Неправильные данные, должно соблюдаться условие l < k')
        if r > k:
            messagebox.showerror('Ошибка', 'Неправильные данные, должно соблюдаться условие r <= k')
        if s > l:
            messagebox.showerror('Ошибка', 'Неправильные данные, должно соблюдаться условие s <= l')
        if r-s > k-l:
            messagebox.showerror('Ошибка', 'Неправильные данные, должно соблюдаться условие r-s <= k-l')

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
        C_pic.place(x=350, y=30)
    if curr == "Размещение с повторением":
        inputK.configure(state="normal")
        txt.configure(state="disabled")
        A_pic.place(x=350, y=30)
    if curr == "Перестановки с повторением":
        inputK.configure(state="disabled")
        txt.configure(state="normal")
        P_pic.place(x=350, y=30)


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
    curr = cb_selectformul.get()

    if int(inputN.get()) < 0 or int(inputK.get()) < 0:
        messagebox.showerror('Ошибка', 'Неправильные данные, введены отрицательные значения')
    elif int(inputN.get()) < int(inputK.get()) and curr == "Сочетание без повторения":
        messagebox.showerror('Ошибка', 'Неправильные данные, должно соблюдаться условие N >= K')
    else:
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
window.title("Лабораторная работа №1. Элементы теории вероятностей.")
window.geometry('1000x400')
window.configure(background='#FFFFFF')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Задание 1')
tab_control.add(tab2, text='Задание 2')
tab_control.pack(expand=1, fill='both')

# Загрузка изображений
A = load_image("accommodation.png")
C = load_image("combination.png")
P = load_image("permutations.png")

# Создание изображений в окне
A_pic = Label(tab1, image=A, anchor=NW)
A_pic.image = A
A_pic.place(x=400, y=60)
A_pic.configure(border='0px')

P_pic = Label(tab1, image=P, anchor=NW)
P_pic.image = P
P_pic.configure(border='0px')

C_pic = Label(tab1, image=C, anchor=NW)
C_pic.image = C
C_pic.configure(border='0px')

# Размещение элементов в окне
label_form = Label(tab1,
                   text="Выберите формулу")
label_form.place(x=10, y=40)

cb_selectformul = ttk.Combobox(tab1,
                               values=[
                                   "Сочетание без повторения",
                                   "Размещение с повторением",
                                   "Перестановки с повторением"], width=35, state="readonly")
cb_selectformul.place(x=14, y=70)
cb_selectformul.current(0)

label_form1 = Label(tab1,
                    text="Введите n")
label_form1.place(x=10, y=110)

inputN = Spinbox(tab1, from_=0, to=10000, width=5)
inputN.place(x=14, y=140)

label_form2 = Label(tab1,
                    text="Введите k ")
label_form2.place(x=150, y=110)

inputK = Spinbox(tab1, from_=0, to=10000, width=5)
inputK.place(x=154, y=140)

label_form2 = Label(tab1,
                    text="Введите подмножество повторяющихся элементов ")
label_form2.place(x=10, y=180)

txt = Entry(tab1, width=30)
txt.place(x=14, y=210)

label_form3 = Label(tab1,
                    text="Результат ")
label_form3.place(x=10, y=290)

result = Entry(tab1, width=160)
result.place(x=10, y=310)

btn_result = Button(tab1, text="Посчитать", command=calc_result)
btn_result.place(x=10, y=250)
btn_result.configure(background='#f9a19a')

change_input_data(None)

cb_selectformul.bind("<<ComboboxSelected>>", change_input_data)

# =====================================================================================================

W = load_image("zadacha.png")
F = load_image("formula.png")

W_pic = Label(tab2, image=W, anchor=NW)
W_pic.image = W
W_pic.place(x=100, y=20)
W_pic.configure(border='0px')

F_pic = Label(tab2, image=F, anchor=NW)
F_pic.image = F
F_pic.place(x=400, y=150)
F_pic.configure(border='0px')

label_k = Label(tab2,
                text="Введите k")
label_k.place(x=10, y=250)

K = Spinbox(tab2, from_=0, to=10000, width=5)
K.place(x=14, y=280)

label_l = Label(tab2,
                text="Введите l")
label_l.place(x=80, y=250)

L = Spinbox(tab2, from_=0, to=10000, width=5)
L.place(x=84, y=280)

label_r = Label(tab2,
                text="Введите r")
label_r.place(x=150, y=250)

R = Spinbox(tab2, from_=0, to=10000, width=5)
R.place(x=154, y=280)

label_s = Label(tab2,
                text="Введите S")
label_s.place(x=220, y=250)

S_ = Spinbox(tab2, from_=0, to=10000, width=5)
S_.place(x=224, y=280)

btn_result2 = Button(tab2, text="Посчитать", command=calc_exer1)
btn_result2.place(x=290, y=270)
btn_result2.configure(background='#f9a19a')

label_result = Label(tab2,
                     text="Результат ")
label_result.place(x=10, y=310)

result2 = Entry(tab2, width=160)
result2.place(x=10, y=330)

# ============================================================================================

window.mainloop()
