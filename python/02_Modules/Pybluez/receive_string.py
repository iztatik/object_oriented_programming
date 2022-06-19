import bluetooth as bt
import time

while input('Search? [y/n]: ') == 'y':
    devices = bt.discover_devices(lookup_names=True)
    print(devices)

bt_id = input('Device ID: ')

def get_address(devices, bt_id):
    address = False
    address = [item[0] for item in devices if(bt_id in item)]
    return address[0]

# Establish the connection
mac_address = get_address(devices, bt_id)
port = 1
socket = bt.BluetoothSocket(bt.RFCOMM)
socket.connect((mac_address, port))


# Get the data
size = 1024
msg = bytearray()
while True:
    msg = socket.recv(1024).decode('utf-8')
    if msg == 'exit': break
    print('Message: ', msg)

socket.close()
