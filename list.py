from tkinter import *
top=Tk()
top.geometry("300x300")
top['bg']="#51E1DC"
Label(top,text="Fruits").pack()
listbox=Listbox(top,height="10")
listbox.insert(1,"Apple")
listbox.insert(2,"Orange")
listbox.insert(3,"Cherry")
listbox.insert(4,"Mango")
listbox.pack()
top.mainloop()