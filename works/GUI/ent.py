import tkinter

w=tkinter.Tk()
w.title("main")
def click():
    l2=tkinter.Label(w,text="answer").pack()
l1=tkinter.Label(w,text="Enter first number",font=(("ArielBold",20))).pack()
et1=tkinter.Entry(w,width=10).pack()
l2=tkinter.Label(w,text="Enter first number",font=(("ArielBold",20))).pack()
et2=tkinter.Entry(w,width=10).pack()
bt=tkinter.Button(w,text="add",bg="red",fg="blue",command=click)

w.geometry("500x300")
w.mainloop()

