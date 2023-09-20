from tkinter import *

root = Tk()
root.title("Test")
root.geometry("400x400")

messageLabel = Label(root,text="")
messageLabel.pack()

def showMessage():
    messageLabel["text"] = "Good Morning"

btn = Button(root, text="Click Me", command=showMessage)
btn.pack()

root.mainloop()


