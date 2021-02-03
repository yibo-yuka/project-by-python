import tkinter as tk
import numpy as np

#x = int(input('first number?:'))
#y = int(input('second number?:'))

win = tk.Tk()
win.title('calculator')
win.geometry("500x500")

e1 = tk.Entry(win, show = None, width = 10)
e1.place(x = 100,y = 170)
e2 = tk.Entry(win, show = None, width = 10)
e2.place(x = 300,y = 170)

def addition():
    x = float(e1.get())
    y = float(e2.get())
    t.insert('end',np.add(x,y))
    #print(np.add(x,y))
def subtract():
    x = float(e1.get())
    y = float(e2.get())
    t.insert('end',np.subtract(x, y))
    #print(np.subtract(x, y))
def multiply():
    x = float(e1.get())
    y = float(e2.get())
    t.insert('end',np.multiply(x, y))
    #print(np.multiply(x, y))
def divide():
    x = float(e1.get())
    y = float(e2.get())
    t.insert('end',np.divide(x, y))
    #print(np.divide(x, y))

lb_1 = tk.Label(win, text = "first number", font = ("Times New Romen", 12), bg = "#FF8811")
lb_1.place(x = 100,y = 150)
lb_2 = tk.Label(win, text = "second number", font = ("Times New Romen", 12), bg = "#FF8811")
lb_2.place(x = 300,y = 150)
lb_3 = tk.Label(win, text = "請先填 first number 和 second number\n再按四則運算中所欲計算方式", font = ("標楷體", 18), bg = "#33BBFF")
lb_3.place(x = 30,y = 10)
b1 = tk.Button(win, text = 'add', width = 10, height = 2 ,command = addition)
b1.place(x = 100,y = 250)
b2 = tk.Button(win, text = 'subtract', width = 10, height = 2 ,command = subtract)
b2.place(x = 300,y = 250)
b3 = tk.Button(win, text = 'multiply', width = 10, height = 2 ,command = multiply)
b3.place(x = 100,y = 300)
b4 = tk.Button(win, text = 'divide', width = 10, height = 2 ,command = divide)
b4.place(x = 300,y = 300)
t = tk.Text(win, height = 3)
t.place(y = 400)

win.mainloop()