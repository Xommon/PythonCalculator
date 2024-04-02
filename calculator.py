from tkinter import*
import math

# Create window
window = Tk()
entry = Entry(window, width=10).grid(row=0, column=0)

# Button methods
def type_number(number):
    print(number)

def clear():
    print("clear")

def operation():
    print("operation")

def decimal():
    print("decimal")

def equals():
    print("equals")

def back():
    print("back")

# Create calculator buttons
for i in range(10):
    if i == 0:
        button = Button(window, text=str(i), command=lambda i=i: type_number(str(i)), width=10, height=5).grid(row=4, column=1)
    else:
        index = i-1
        button = Button(window, text=str(i), command=lambda i=i: type_number(str(i)), width=10, height=5).grid(row=math.floor(index/3)+1, column=index%3)
for i in range(4):
    operations = ['+', '-', '*', '/']
    button = Button(window, text=operations[i], command=operation, width=10, height=5).grid(row=i+1, column=4)
button = Button(window, text='C', command=clear, width=10, height=5).grid(row=4, column=0)
button = Button(window, text='.', command=decimal, width=10, height=5).grid(row=4, column=2)
button = Button(window, text='=', command=equals, width=10, height=5).grid(row=5, column=1)
button = Button(window, text='<-', command=back, width=10, height=5).grid(row=5, column=2)

window.mainloop()