from tkinter import *
 
root = Tk() 
root.geometry("300x160") 
root.title('Frames')

# Top frame
l1 = Label(root, text ='Top frame', font = "80") 
l1.pack(side=TOP) 

top_frame = Frame(root) 
top_frame.pack(side=TOP) 

# Medium frame
medium_frame = Frame(root) 
medium_frame.pack(side = TOP) 

l2 = Label(medium_frame, text='Medium frame', font='80')
l2.pack(side=TOP)

left_frame = Frame(medium_frame)
left_frame.pack(side=LEFT)

right_frame = Frame(medium_frame)
right_frame.pack(side=RIGHT)

# Bottom frame
bottom_frame = Frame(root)
bottom_frame.pack(side=TOP)

l3 = Label(bottom_frame, text='Bottom frame', font='80')
l3.pack(side=TOP)



# Buttons
button1 = Button(top_frame, text ="Block1", fg ="red") 
button1.pack(side = LEFT) 

button2 = Button(top_frame, text ="Block2", fg ="brown") 
button2.pack(side = LEFT) 

button3 = Button(top_frame, text ="Block3", fg ="blue") 
button3.pack(side = LEFT) 

button4 = Button(left_frame, text ="Block4", fg ="orange") 
button4.pack(side = BOTTOM) 

button5 = Button(left_frame, text ="Block5", fg ="orange") 
button5.pack(side = BOTTOM) 

button6 = Button(left_frame, text ="Block6", fg ="orange") 
button6.pack(side = BOTTOM) 

button7 = Button(right_frame, text ="Block7", fg ="green") 
button7.pack(side = TOP) 

button8 = Button(right_frame, text ="Block8", fg ="green") 
button8.pack(side = TOP) 

button9 = Button(right_frame, text ="Block9", fg ="green") 
button9.pack(side = TOP) 

button10 = Button(bottom_frame, text ="Block10", fg ="red") 
button10.pack(side = TOP, fill=X) 




root.mainloop()
