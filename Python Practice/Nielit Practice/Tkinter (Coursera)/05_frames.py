from tkinter import*
root = Tk()
root.geometry("400x300")
root.title("Frames")

# Builds the frame
frame = Frame(root)
frame.pack()

# Setup the different Frame slides
leftframe = Frame(root)
leftframe.pack(side=LEFT)
rightframe = Frame(root)
rightframe.pack(side=RIGHT)
topframe = Frame(root)
topframe.pack(side=TOP)
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

# Assigning the buttons to the different locations
b1 = Button(topframe, text="Button1")
b1.pack(side=LEFT)
b1 = Button(bottomframe, text="Button1")
b1.pack(side=RIGHT)
b1 = Button(rightframe, text="Button1")
b1.pack(side=LEFT)
b1 = Button(leftframe, text="Button1")
b1.pack(side=RIGHT)

root.mainloop()