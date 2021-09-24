import serial
import time

timeout = time.time() + 30
with serial.Serial('/dev/ttyUSB0', 115200, timeout=1) as ser:
    while(((x := ser.readline()) != b'Hello world!\r\n') and (t := (timeout > time.time()))):
        print(x)

assert(t)
print("Brilliant!")
    

