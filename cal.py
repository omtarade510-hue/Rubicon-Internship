import tkinter
from tkinter import messagebox
from tkinter import *
top = tkinter.Tk()
top.geometry("300x400")
top.title("Calculator")
top['bg']="#51E1DC"
int1=IntVar()
int2=IntVar()
Label(top,text="First number",width="13").place(x=50,y=50)
ent=Entry(top,textvariable=int1).place(x=150,y=50)
Label(top,text="Second number",width="13").place(x=50,y=100)
ent1=Entry(top, textvariable=int2).place(x=150,y=100)
def add1():
    a=int1.get()
    b=int2.get()
    messagebox.showinfo("Result: ",(a+b))
btn=Button(top,text="Addition",command=add1).place(x=50,y=150)
def sub1():
    a=int1.get()
    b=int2.get()
    messagebox.showinfo("Result: ",(a-b))
btn=Button(top,text="Stubtraction",command=sub1).place(x=50,y=200)
def mul1():
    a=int1.get()
    b=int2.get()
    messagebox.showinfo("Result: ",(a*b))
btn=Button(top,text="multiplication",command=mul1).place(x=50,y=250)
def div1():
    a=int1.get()
    b=int2.get()
    messagebox.showinfo("Result: ",(a/b))
btn=Button(top,text="Division",command=div1).place(x=50,y=300)
top.mainloop()