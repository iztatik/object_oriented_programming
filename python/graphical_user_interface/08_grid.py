#!/usr/bin/env python3
import tkinter as tk

class Teach_pendant():
    def __init__(self):
        self.__root = tk.Tk()

        # Buttons
        self.__connect_bttn = tk.Button(self.__root, text = 'Connect')
        self.__front_bttn = tk.Button(self.__root, text = 'Forward')
        self.__back_bttn = tk.Button(self.__root, text = 'Backward')
        self.__right_bttn = tk.Button(self.__root, text = 'Right')
        self.__left_bttn = tk.Button(self.__root, text = 'Left')
        self.__stop_bttn = tk.Button(self.__root, text = 'Stop')
        self.__sensor_bttn = tk.Button(self.__root, text = 'Read sensors')
        self.__search_bttn = tk.Button(self.__root, text = 'Search')

        # Entries
        self.__bt_entry = tk.Entry(self.__root)

        # Scales 
        self.__speed_scale = tk.Scale(self.__root, from_=10, to=100, resolution=5)

        # Label/frame
        self.__status_frame = tk.LabelFrame(self.__root, text='Robot status')
        self.__status_label = tk.Label(self.__status_frame, text='Relevant\ninformation\nof the\nrobot', justify=tk.LEFT)


    def launch(self):
        # Buttons
        self.__connect_bttn.grid(row=0, column=0)
        self.__left_bttn.grid(row=3, column=0)
        self.__front_bttn.grid(row=2, column=1)
        self.__stop_bttn.grid(row=3, column=1)
        self.__back_bttn.grid(row=4, column=1)
        self.__right_bttn.grid(row=3, column=2)
        self.__sensor_bttn.grid(row=4, column=4, columnspan=7)
        self.__search_bttn.grid(row=1, column=0)

        # Entries
        self.__bt_entry.grid(row=0, column=1, columnspan=2)

        # Scales
        self.__speed_scale.grid(row=1, column=3, rowspan=4)
        
        # Frame/label
        self.__status_frame.grid(row=0, column=4, rowspan=3, columnspan=7)
        self.__status_label.pack()

        self.__root.mainloop()
        return


if __name__=='__main__':
    my_pendant = Teach_pendant()
    my_pendant.launch()

