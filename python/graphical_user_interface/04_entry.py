from tkinter import *

def message():
    print(entry.get())

root = Tk()
root.geometry('250x80')

# Entry widget
entry = Entry(root)
entry.pack(pady = 10)

# Button
button = Button(root, text='Button', command = message)
button.pack(side = LEFT)

root.mainloop()
