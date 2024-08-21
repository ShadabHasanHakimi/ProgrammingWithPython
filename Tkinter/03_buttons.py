from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text="You clicked Button!").pack()

# state="disabled" turns button disabled
b1 = Button(root, text="Button1", padx="50", command=myClick).pack()

root.mainloop()