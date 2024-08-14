from tkinter import *

root = Tk()
root.geometry("400x150")
root.title("Buttons")

def write_message():
    print("Welcome to python!")
def quit():
    root.destroy()

# Create the button object with red text
button = Button(root, 
                text="QUIT", 
                fg="red", 
                command=root.quit)
# puts button in left side
button.pack(side=LEFT)

# Creates a second button that displays a message in console
# It displays message through function write_message
message = Button(root,
                 text="Welcome Message!",
                 fg="green",
                 command=write_message)
message.pack()

button3 = Button(root,
                 text="TOP",
                 fg="blue")
button3.pack(side=TOP)

button3 = Button(root,
                 text="BOTTOM",
                 fg="black")
button3.pack(side=BOTTOM)

root.mainloop()