from tkinter import *

a = Tk()
a.title("Calculadora")
a.configure(bg="yellow")
e = Entry(a, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)


Button(a, text="0", padx=40, pady=5, command=lambda: e.insert(END, "0")).grid(row=1, column=0)
Button(a, text="1", padx=40, pady=5, command=lambda: e.insert(END, "1")).grid(row=1, column=1)
Button(a, text="2", padx=40, pady=5, command=lambda: e.insert(END, "2")).grid(row=2, column=0)
Button(a, text="3", padx=40, pady=5, command=lambda: e.insert(END, "3")).grid(row=2, column=1)
Button(a, text="4", padx=40, pady=5, command=lambda: e.insert(END, "4")).grid(row=3, column=0)
Button(a, text="5", padx=40, pady=5, command=lambda: e.insert(END, "5")).grid(row=3, column=1)
Button(a, text="6", padx=40, pady=5, command=lambda: e.insert(END, "6")).grid(row=4, column=0)
Button(a, text="7", padx=40, pady=5, command=lambda: e.insert(END, "7")).grid(row=4, column=1)
Button(a, text="8", padx=40, pady=5, command=lambda: e.insert(END, "8")).grid(row=5, column=0)
Button(a, text="9", padx=40, pady=5, command=lambda: e.insert(END, "9")).grid(row=5, column=1)
Button(a, text="÷", padx=40, pady=5, command=lambda: e.insert(END, "/")).grid(row=1, column=2)
Button(a, text="+", padx=40, pady=5, command=lambda: e.insert(END, "+")).grid(row=2, column=2)
Button(a, text="x", padx=40, pady=5, command=lambda: e.insert(END, "*")).grid(row=3, column=2)
Button(a, text="-", padx=40, pady=5, command=lambda: e.insert(END, "-")).grid(row=4, column=2)
Button(a, text="=", padx=40, pady=5, command=lambda: e.insert(END, "=" + str(eval(e.get())))).grid(row=5, column=2)
Button(a, text="clear", padx=30, pady=5, command=lambda: e.delete(0, END)).grid(row=6)
mainloop()
