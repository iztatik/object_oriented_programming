from tkinter import *

# Root element
root = Tk()
root.geometry("200x150")

# Listbox
listbox = Listbox(root, selectmode=SINGLE)

for i in range(1, 21):
    listbox.insert(i, f'Option_{i}')

# Scrollbar
scrollbar = Scrollbar(root, command = listbox.yview)


listbox.config(yscrollcommand = scrollbar.set)

listbox.pack(side=LEFT, fill=BOTH)
scrollbar.pack(side=LEFT, fill=BOTH)

root.title('Listbox')
root.mainloop()
