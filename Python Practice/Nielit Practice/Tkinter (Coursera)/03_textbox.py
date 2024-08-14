# One of the most important features
from tkinter import*
root = Tk()
root.geometry("300x300")
root.title("TextBoxes")

def insertText():
    user_input = textField1.get("1.0", END) # read from 1 textbox
    textField2.insert(END, user_input) # insert into another textbox
    
user_input = StringVar()

label1 = Label(root, text="Enter your name: ", width=15)
label1.grid(row=1, column=1)

textField1 = Text(root, height=1, width=16, bg="yellow")
textField1.grid(row=1, column=2)

b1 = Button(root, text="Update", width=10, bg="red", command=lambda: insertText())
b1.grid(row=2, column=2)

textField2 = Text(root, height=1, width=16, bg="pink")
textField2.grid(row=3, column=2)

root.mainloop()