import tkinter
from tkinter.ttk import *
w=tkinter.Tk()
w.title("Main")

l=tkinter.Label(w,text="Languages")
rd1=Radiobutton(w,text="python",value=1)
rd2=Radiobutton(w,text="Java",value=2)
rd3=Radiobutton(w,text="PHP",value=3)
l.grid(row=0,column=1)
rd1.grid(row=1,column=0)
rd2.grid(row=1,column=1)
rd3.grid(row=1,column=2)
w.geometry("400x300")
w.mainloop()