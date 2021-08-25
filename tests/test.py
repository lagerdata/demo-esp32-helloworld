import serial
import time

timeout = time.time() + 15
with serial.Serial('/dev/ttyUSB2', 115200, timeout=1) as ser:
    while(((x := ser.readline()) != b'Hello world!\r\n') and (t := (timeout > time.time()))):
        print(x)

assert(t)
print("Brilliant!")
    

