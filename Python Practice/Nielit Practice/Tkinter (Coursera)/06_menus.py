from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("Menu")

# Creating menubar
menubar = Menu(root)

# Adding file menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New File", command=None)
file.add_command(label="Open...", command=None)
file.add_command(label="Save", command=None)
file.add_separator()
file.add_command(label="Exit", command=root.destroy)

# Adding help menu
helpInfo = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Contact Help",menu=helpInfo)
helpInfo.add_command(label="Help Lessons", menu=None)
helpInfo.add_separator()
helpInfo.add_command(label="About", menu=None)

# Display menu
root.config(menu=menubar)
mainloop()
