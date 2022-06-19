import bluetooth as bt

serverMACAddress = '08:3A:F2:AC:3C:0A'
port = 1
s = bt.BluetoothSocket(bt.RFCOMM)
s.connect((serverMACAddress, port))
while 1:
    text = input('Message: ') # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
s.close()
