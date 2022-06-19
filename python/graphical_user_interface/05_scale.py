from tkinter import *

def message(v):
    print(v)

# Root element
root = Tk()
root.geometry('150x40')

# Scale widget
v = DoubleVar()
scale = Scale(root, variable=v, from_=-10.0, to=10.0, resolution=0.5, command=message, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

root.title('Scale')
root.mainloop()

