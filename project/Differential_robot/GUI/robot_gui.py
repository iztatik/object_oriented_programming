#!/usr/bin/env python3

import tkinter as tk
import bluetooth as bt
import time

class Teach_pendant():
    def __init__(self):
        self.__root = tk.Tk()

        # Bluetooth
        self.__mac_address = None
        self.__PORT = 1
        self.__socket = bt.BluetoothSocket(bt.RFCOMM)
        self.__devices = None

        # Variables
        self.__speed = tk.DoubleVar()
        self.__direction = 'Stop'
        self.__temperature = '-'
        self.__presion = '-'
        self.__connection = 'Disconected'
        self.__distance = '-'
        self.__humidity = '-'

        # Other widgets variables
        self.__entry_text = tk.StringVar()

        # Buttons
        self.__connect_bttn = tk.Button(self.__root, text = 'Connect', command=self.__bt_connect)
        self.__front_bttn = tk.Button(self.__root, text = 'Forward', command=self.__bttn_1)
        self.__back_bttn = tk.Button(self.__root, text = 'Backward', command=self.__bttn_2)
        self.__right_bttn = tk.Button(self.__root, text = 'Right', command=self.__bttn_3)
        self.__left_bttn = tk.Button(self.__root, text = 'Left', command=self.__bttn_4)
        self.__stop_bttn = tk.Button(self.__root, text = 'Stop', command=self.__bttn_5)
        self.__sensor_bttn = tk.Button(self.__root, text = 'Read sensors', command=self.__bttn_6)
        self.__search_bttn = tk.Button(self.__root, text = 'Search', command=self.__bt_search)

        # Entries
        self.__bt_entry = tk.Entry(self.__root, textvariable=self.__entry_text) 

        # Scales 
        self.__speed_scale = tk.Scale(self.__root, from_=10, to=100, resolution=5, variable=self.__speed, command=self.__send_speed)

        # Label/frame
        self.__status_frame = tk.LabelFrame(self.__root, text='Robot status')
        self.__status_label = tk.Label(self.__status_frame, text='Press search...', justify=tk.LEFT)


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

    # Bluetooth
    def __bt_search(self):
        self.__status_label.config(text='Searching...')
        devices = bt.discover_devices(lookup_names=True)
        message = 'Devices: \n'
        for device in devices:
            message = message + '- ' + str(device[1]) + '\n'
        self.__status_label.config(text=message)
        self.__devices = devices
        return

    def __bt_connect(self):
        self.__status_label.config(text='Connecting...')
        address = [item[0] for item in self.__devices if(self.__entry_text.get() in item)]
        self.__mac_address = address[0]
        self.__socket.connect((self.__mac_address, self.__PORT))
        self.__connection = 'Connected'
        self.__set_status()
        return

    # Buttons
    def __button(fun):
        def wrapper(self):
            fun(self)
            self.__send_bt('direction', self.__direction)
            self.__set_status()
        return wrapper 

    @__button
    def __bttn_1(self): self.__direction = 'Forward'

    @__button
    def __bttn_2(self): self.__direction = 'Backward'

    @__button
    def __bttn_3(self): self.__direction = 'CW'

    @__button
    def __bttn_4(self): self.__direction = 'CCW'

    @__button
    def __bttn_5(self): self.__direction = 'Stop'

    def __bttn_6(self): 
        self.__send_bt('sensors', 'all')
        data = self.__socket.recv(1024).decode('utf-8')
        data = data.split('/')
        self.__temperature = data[0] 
        self.__humidity = data[1]
        self.__presion = data[2]
        self.__distance = data[3]
        time.sleep(1)
 
        self.__set_status()
        return


    def __send_speed(self, v):
        self.__send_bt('velocity', v)
        self.__set_status()
        return

    def __send_bt(self, key, data):
        self.__socket.send(str(key) + '/')
        self.__socket.send(str(data) + '/')
        return

    def __set_status(self):
        connection = 'Connection: ' + self.__connection + '\n'
        direction = 'Direction: ' + self.__direction + '\n'
        speed = 'Speed: {}% \n'.format(self.__speed.get())
        temperature = 'Temperature: {}° \n'.format(self.__temperature)
        presion = 'Presion: {} \n'.format(self.__presion)
        distance = 'Distance: {} \n'.format(self.__distance)
        humidity = 'Humidity: {}'.format(self.__humidity)

        text = connection + direction + speed + temperature + presion + distance + humidity
        self.__status_label.config(text=text)
        return


if __name__=='__main__':
    my_pendant = Teach_pendant()
    my_pendant.launch()

