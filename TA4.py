from tkinter import *

root = Tk()
root.title("Test")
root.geometry("400x400")

nameInput = Entry(root)
nameInput.pack()

messageLabel = Label(root,text="")
messageLabel.pack()

def showMessage():
    name = nameInput.get()
    messageLabel["text"] = name + "! You are awesome!"

btn = Button(root, text="Click Me", command=showMessage)
btn.pack()

root.mainloop()

