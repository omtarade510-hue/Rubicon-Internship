import tkinter
from tkinter import messagebox
from tkinter import *
top=tkinter.Tk()
# Creating the frame
top.geometry("325x200")
# Giving the title
top.title("Om")
# Background Colour
top['bg']="#51E1DC"
# Add text
uname = Label(top,text="This is the Label").place(x=30,y=50)
# Creating the button
# btn=Button(top,text="Click Me").pack()
# Message display
def myfun():
    messagebox.showinfo("Title","You Clicked this Button")
# Alert 
btn=Button(top,text="Click Me",command=myfun).pack()
# Text box
Label(top,text="First Number",width="13").place(x=50,y=100)
ent=Entry(top).place(x=150,y=100)
top.mainloop()