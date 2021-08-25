import serial
with serial.Serial('/dev/ttyUSB2', 115200, timeout=1) as ser:
    while((x := ser.readline()) != b'Hello world!\r\n'):
        print(x)
print("Brilliant!")
    

