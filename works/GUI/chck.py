import tkinter
from tkinter.ttk import *
w=tkinter.Tk()
w.title("main")

l=tkinter.Label(w,text="Check")
val=tkinter.BooleanVar()
val.set(False)
c=Checkbutton(w,text="Select",var=val)
l.grid(row=0,column=1)
c.grid(row=1,column=1)
w.geometry("500x400")
w.mainloop()

