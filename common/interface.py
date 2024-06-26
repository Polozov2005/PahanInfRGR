from tkinter import *
from tkinter import messagebox
from ctypes import windll

import equation
import initialization
import saving

def interface_initialization():
    root.mainloop()

windll.shcore.SetProcessDpiAwareness(1) # Для отсутствия размытия интерфейса
root = Tk()
root.geometry("1600x900")
root.title("РГР")
root.resizable(False, False)

frm_scheme = Frame(
    root,
)
frm_scheme.place(
    x=0,
    y=0,
    width = 800,
    height = 900
)

frm_checkbutton = Frame(
    root,
)
frm_checkbutton.place(
    x=800,
    y=0,
    width = 800,
    height = 160
)

frm_Y = Frame(
    root,
)
frm_Y.place(
    x=800,
    y=160,
    width = 800,
    height = 160
)

frm_E = Frame(
    root,
)
frm_E.place(
    x=800,
    y=320,
    width = 800,
    height = 160
)

frm_solveandsave = Frame(
    root,
)
frm_solveandsave.place(
    x=800,
    y=480,
    width = 800,
    height = 100
)

frm_X = Frame(
    root,
)
frm_X.place(
    x=800,
    y=580,
    width = 800,
    height = 320
)

### Схема
scheme = PhotoImage(file="gfx/scheme.png")

label_scheme = Label(
    frm_scheme,
    image=scheme
)

label_scheme.grid(
    row=0,
    column=0
)


### Выключатели
enabled_checkbutton_1 = IntVar(value=1)
checkbutton_1 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_1,
    text='Выключатель 1'
)
checkbutton_1.grid(
    row=0,
    column=0
)

enabled_checkbutton_2 = IntVar(value=1)
checkbutton_2 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_2,
    text='Выключатель 2'
)
checkbutton_2.grid(
    row=1,
    column=0
)

enabled_checkbutton_3 = IntVar(value=1)
checkbutton_3 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_3,
    text='Выключатель 3'
)
checkbutton_3.grid(
    row=2,
    column=0
)

enabled_checkbutton_4 = IntVar(value=1)
checkbutton_4 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_4,
    text='Выключатель 4'
)
checkbutton_4.grid(
    row=3,
    column=0
)

enabled_checkbutton_5 = IntVar(value=1)
checkbutton_5 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_5,
    text='Выключатель 5'
)
checkbutton_5.grid(
    row=4,
    column=0
)

enabled_checkbutton_6 = IntVar(value=1)
checkbutton_6 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_6,
    text='Выключатель 6'
)
checkbutton_6.grid(
    row=0,
    column=1
)

enabled_checkbutton_7 = IntVar(value=1)
checkbutton_7 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_7,
    text='Выключатель 7'
)
checkbutton_7.grid(
    row=1,
    column=1
)

enabled_checkbutton_8 = IntVar(value=1)
checkbutton_8 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_8,
    text='Выключатель 8'
)
checkbutton_8.grid(
    row=2,
    column=1
)

enabled_checkbutton_10 = IntVar(value=1)
checkbutton_10 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_10,
    text='Выключатель 10'
)
checkbutton_10.grid(
    row=0,
    column=2
)

enabled_checkbutton_11 = IntVar(value=1)
checkbutton_11 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_11,
    text='Выключатель 11'
)
checkbutton_11.grid(
    row=1,
    column=2
)

enabled_checkbutton_21 = IntVar(value=1)
checkbutton_21 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_21,
    text='Выключатель 21'
)
checkbutton_21.grid(
    row=0,
    column=3
)

enabled_checkbutton_22 = IntVar(value=1)
checkbutton_22 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_22,
    text='Выключатель 22'
)
checkbutton_22.grid(
    row=1,
    column=3
)

enabled_checkbutton_23 = IntVar(value=1)
checkbutton_23 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_23,
    text='Выключатель 23'
)
checkbutton_23.grid(
    row=2,
    column=3
)

enabled_checkbutton_24 = IntVar(value=1)
checkbutton_24 = Checkbutton(
    frm_checkbutton,
    variable=enabled_checkbutton_24,
    text='Выключатель 24'
)
checkbutton_24.grid(
    row=3,
    column=3
)


### Y
image_Y = PhotoImage(file="gfx/Y.png")
label_Y = Label(
    frm_Y,
    image=image_Y
)
label_Y.pack()

### E
image_E = PhotoImage(file="gfx/E.png")
label_E = Label(
    frm_E,
    image=image_E
)
label_E.pack()


### Вывод кнопки для расчёта и сохранения
def click_solve():    
    A_matrix = initialization.A()['matrix']
    Y_matrix = initialization.Y()['matrix']
    I_matrix = initialization.I()['matrix']
    E_matrix = initialization.E()['matrix']

    if enabled_checkbutton_1.get() == 0:
        i = 5
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_2.get() == 0:
        i = 6
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_3.get() == 0:
        i = 9
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_4.get() == 0:
        i = 10
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_5.get() == 0:
        i = 13
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_6.get() == 0:
        i = 14
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_7.get() == 0:
        i = 15
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_8.get() == 0:
        i = 16
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_10.get() == 0:
        i = 30
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_11.get() == 0:
        i = 29
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_21.get() == 0:
        i = 7
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_22.get() == 0:
        i = 8
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_23.get() == 0:
        i = 21
        Y_matrix[i - 1, i - 1] = 0

    if enabled_checkbutton_24.get() == 0:
        i = 22
        Y_matrix[i - 1, i - 1] = 0

    U_list = equation.U(
        A=A_matrix,
        Y=Y_matrix,
        I=I_matrix,
        E=E_matrix
    )['list']

    if isinstance(U_list, int) and U_list == 0:
        messagebox.showerror(
            title='Ошибка в ходе решения уравнения',
            message='В ходе решения на главной диагонали оказался ноль - система не совместна'
        )

    else:
        X_list = equation.X(U_list)['list']

        saving.X(X_list=X_list)
        
        label_X_1["text"] = 'X1 = '+ str(X_list[1]) + ' кВ'
        label_X_2["text"] = 'X2 = '+ str(X_list[2]) + ' кВ'
        label_X_3["text"] = 'X3 = '+ str(X_list[3]) + ' кВ'
        label_X_4["text"] = 'X4 = '+ str(X_list[4]) + ' кВ'
        label_X_5["text"] = 'X5 = '+ str(X_list[5]) + ' кВ'
        label_X_6["text"] = 'X6 = '+ str(X_list[6]) + ' кВ'
        label_X_7["text"] = 'X7 = '+ str(X_list[7]) + ' кВ'
        label_X_8["text"] = 'X8 = '+ str(X_list[8]) + ' кВ'
        label_X_9["text"] = 'X9 = '+ str(X_list[9]) + ' кВ'
        label_X_10["text"] = 'X10 = '+ str(X_list[10]) + ' кВ'


btn_solve = Button(
    frm_solveandsave,
    text='Рассчитать и сохранить',
    command=click_solve
)
btn_solve.grid(row=0, column=0)
frm_solveandsave.columnconfigure(index=0, weight=1)
frm_solveandsave.rowconfigure(index=0, weight=1)

### X
label_X_1 = Label(
    frm_X,
    text='X1 = 0 кВ'
)

label_X_1.grid(
    row=0,
    column=0
)

label_X_2 = Label(
    frm_X,
    text='X2 = 0 кВ'
)

label_X_2.grid(
    row=1,
    column=0
)

label_X_3 = Label(
    frm_X,
    text='X3 = 0 кВ'
)

label_X_3.grid(
    row=2,
    column=0
)

label_X_4 = Label(
    frm_X,
    text='X4 = 0 кВ'
)

label_X_4.grid(
    row=3,
    column=0
)

label_X_5 = Label(
    frm_X,
    text='X5 = 0 кВ'
)

label_X_5.grid(
    row=4,
    column=0
)

label_X_6 = Label(
    frm_X,
    text='X6 = 0 кВ'
)

label_X_6.grid(
    row=5,
    column=0
)

label_X_7 = Label(
    frm_X,
    text='X7 = 0 кВ'
)

label_X_7.grid(
    row=6,
    column=0
)

label_X_8 = Label(
    frm_X,
    text='X8 = 0 кВ'
)

label_X_8.grid(
    row=7,
    column=0
)

label_X_9 = Label(
    frm_X,
    text='X9 = 0 кВ'
)

label_X_9.grid(
    row=8,
    column=0
)

label_X_10 = Label(
    frm_X,
    text='X10 = 0 кВ'
)

label_X_10.grid(
    row=9,
    column=0
)

interface_initialization()