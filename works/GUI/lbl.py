import tkinter

w=tkinter.Tk()
w.title("guilabel")
l1=tkinter.Label(w,text="Python",font=(("ArielBold",30)))
l2=tkinter.Label(w,text="C++",font=(("ArielBold",30)))
l3=tkinter.Label(w,text="Java",font=(("ArielBold",30)))
l1.grid(row=0,column=0)
l2.grid(row=1,column=1)
l3.grid(row=0,column=2)
w.geometry("500x300")
w.mainloop()
