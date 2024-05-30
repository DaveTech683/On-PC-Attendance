from tkinter import *

root = Tk()

sum_screen = Entry(root)
sum_screen.place(x=80, y = 5)

lbl = Label(root, text="Enter First Num:")
lbl.place(x = 80, y = 30)

ent1 = Entry(root)
ent1.place(x=80, y = 50)

lbl2 = Label(root, text="Enter Operator:")
lbl2.place(x = 80, y = 70)

ent2 = Entry(root)
ent2.place(x=80, y = 90)

lbl3 = Label(root, text="Enter Second Num:")
lbl3.place(x = 80, y = 110)

ent3 = Entry(root)
ent3.place(x=80, y = 130)


def cal():
    num1 = int(ent1.get())
    num2 = int(ent3.get())
    opr = ent2.get()

    if opr == "+":
        suming = num1+num2
        if sum_screen == "":
            sum_screen.insert(0, suming)
        else:
            sum2 = ("After the existing answer",suming)
            sum_screen.insert(0, sum2)   
    elif opr == "-":
        suming = num1-num2
        sum_screen.insert(0, suming)
    elif opr == "*":
        suming = num1*num2
        sum_screen.insert(0, suming)

btn = Button(root, text="Calculate", command=lambda:cal())
btn.place(x = 100, y = 160)


root.mainloop()