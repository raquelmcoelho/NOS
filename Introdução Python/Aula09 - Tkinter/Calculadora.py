from tkinter import *

a = Tk()
a.title("Calculadora")
a.configure(bg="yellow")
e = Entry(a, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)


def clear():
    e.delete(0, END)


def result():
    try:
        return e.insert(END, " = " + str(eval(e.get())))
    except SyntaxError:
        pass


def insert(char):
    if "=" in e.get():
        clear()
    e.insert(END, char)


def function(char):
    return lambda: insert(char)


content = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "*", "+", "-"]
column = 0
row = 0
for i in content:
    if content.index(i) % 2 == 0:
        column = 0
        row += 1
    else:
        column = 1
    if content.index(i) > 9:
        row = content.index(i) % 9
        column = 2
    Button(a, text=i, padx=40, pady=5, command=function(i)).grid(row=row, column=column)

Button(a, text="=", padx=40, pady=5, command=lambda: result()).grid(row=5, column=2)
Button(a, text="clear", padx=30, pady=5, command=lambda: clear()).grid(row=6)
mainloop()
