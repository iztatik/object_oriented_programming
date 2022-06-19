from tkinter import *
 
# Function binded to the button
def message():
    print("Hello World")
 
# Root element
root = Tk()
root.geometry("180x60")
 
# Button widget
button = Button(root, text = "Button1", command = message)

# Pack the widgets
button.pack(pady = 15)

# Display
root.title('Button')
root.mainloop()
