from tkinter import *

root = Tk()
root.title("Basic Calculator")
root.geometry("275x235")
root.minsize(275, 235)
root.maxsize(275, 235)

entry = Entry(root)
entry.grid(row=0, column=0, columnspan=3, padx=8, pady=8)


def click(number):
    entry.delete(0, END)
    entry.insert(0, number)
    print(number)
    return


def add():
    return


def subtract():
    return


def multiply():
    return


def divide():
    return


# Define Buttons
button_0 = Button(root, text=0, width=3, height=2,command=lambda: click(0))
button_1 = Button(root, text=1, width=3, height=2, command=lambda: click(1))
button_2 = Button(root, text=2, width=3, height=2, command=lambda: click(2))
button_3 = Button(root, text=3, width=3, height=2, command=lambda: click(3))
button_4 = Button(root, text=4, width=3, height=2, command=lambda: click(4))
button_5 = Button(root, text=5, width=3, height=2, command=lambda: click(5))
button_6 = Button(root, text=6, width=3, height=2, command=lambda: click(6))
button_7 = Button(root, text=7, width=3, height=2, command=lambda: click(7))
button_8 = Button(root, text=8, width=3, height=2, command=lambda: click(8))
button_9 = Button(root, text=9, width=3, height=2, command=lambda: click(9))
button_dot = Button(root, text='.', width=3, height=2, command=lambda: click('.'))
button_add = Button(root, text='+', width=3, height=2, command=add)
button_subtract = Button(root, text='-', width=3, height=2, command=add)
button_multiply = Button(root, text='x', width=3, height=2, command=add)
button_divide = Button(root, text='/', width=3, height=2, command=add)
button_equal = Button(root, text='=', width=3, height=2, command=add)
button_clear = Button(root, text='clear', width=3, height=2, command=add)

# Placing Buttons
button_clear.grid(row=0, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=1)
button_dot.grid(row=4, column=0)
button_equal.grid(row=4, column=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()
