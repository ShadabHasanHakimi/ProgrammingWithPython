from tkinter import *

# for image use Toplevel()
root = Toplevel()
root.title("PythonGuides")

photo = PhotoImage(file="./bootstrap.png")
photo = photo.subsample(2)
lbl = Label(root, image=photo)
lbl.pack()

mainloop()