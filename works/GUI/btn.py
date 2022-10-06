import tkinter

w=tkinter.Tk()
w.title("guibutton")
def click1():
    l2=tkinter.Label(w,text="python")
    l2.grid(row=2,column=1)
def click2():
    l3=tkinter.Label(w,text="PYTHON")
    l3.grid(row=2,column=1)

l1=tkinter.Label(w,text="testing button",font=(("ArielBold",20)))
bt1=tkinter.Button(w,text="lower",bg="red",fg="blue",command=click1)
bt2=tkinter.Button(w,text="upper",bg="red",fg="blue",command=click2)
l1.grid(row=0,column=1)
bt1.grid(row=1,column=0)
bt2.grid(row=1,column=2)
w.geometry("500x300")
w.mainloop()
