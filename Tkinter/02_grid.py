from tkinter import *
root = Tk()

myLabel1 = Label(root, text="Label 1")
myLabel2 = Label(root, text="Label 2")

# Grid system
myLabel1.grid(row=0, column=1)
myLabel2.grid(row=1, column=2)

root.mainloop()