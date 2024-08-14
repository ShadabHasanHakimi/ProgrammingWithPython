from tkinter import *
root = Tk() # Creates a root window where all the widgets go
# Set the size of the window
root.geometry("700x350")
label1 = Label(root, text="Tkinter is used for building GUI using python!")
label1.pack() # put the label into the window

# set font and its size
label2 = Label(root, text="Python is Amazing!!!", font=("Helvetica, 14"))
# set font color
label2.config(fg="green")
label2.pack()
root.mainloop() # start the event loop