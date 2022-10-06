import tkinter

from tkinter.scrolledtext import ScrolledText
w=tkinter.Tk()
w.title("Main")

s=ScrolledText(w,width=20,height=8)
s.grid(row=0,column=1)
w.geometry("500x400")
w.mainloop()