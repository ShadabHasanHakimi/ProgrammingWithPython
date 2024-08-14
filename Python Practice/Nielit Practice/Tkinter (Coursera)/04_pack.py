from tkinter import*
root = Tk()
root.geometry("300x500")
root.title("Layouts")

# Simple pack
label1 = Label(root, text="This", fg="white", bg="red")
label1.pack()
label2 = Label(root, text="is", fg="white", bg="green")
label2.pack()
label3 = Label(root, text="simple label", fg="white", bg="blue")
label3.pack()

# for extra line
l1 = Label(root, text="")
l1.pack()

# fill=X pack
label1 = Label(root, text="This",fg="white", bg="red")
label1.pack(fill=X)
label2 = Label(root, text="is",fg="white", bg="green")
label2.pack(fill=X)
label3 = Label(root, text="pack(fill=X)",fg="white", bg="blue")
label3.pack(fill=X)

# for extra line
l1 = Label(root, text="")
l1.pack()

# fill=X, padx=15 pack
label1 = Label(root, text="This",fg="white", bg="red")
label1.pack(fill=X, padx=15)
label2 = Label(root, text="is",fg="white", bg="green")
label2.pack(fill=X, padx=15)
label3 = Label(root, text="pack(fill=X, padx=15)",fg="white", bg="blue")
label3.pack(fill=X, padx=15)

# for extra line
l1 = Label(root, text="")
l1.pack()

# fill=X, padx=15 pack
label1 = Label(root, text="This",fg="white", bg="red")
label1.pack(fill=X, pady=15)
label2 = Label(root, text="is",fg="white", bg="green")
label2.pack(fill=X, pady=15)
label3 = Label(root, text="pack(fill=X, pady=15)",fg="white", bg="blue")
label3.pack(fill=X, pady=15)

# for extra line
l1 = Label(root, text="")
l1.pack()

# fill=X, padx=15 pack
label1 = Label(root, text="This",fg="white", bg="red")
label1.pack(fill=X, pady=15, side=LEFT)
label2 = Label(root, text="is",fg="white", bg="green")
label2.pack(fill=X, pady=15, side=LEFT)
label3 = Label(root, text="pack",fg="white", bg="blue")
label3.pack(fill=X, pady=15, side=RIGHT)

root.mainloop()