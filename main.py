from project.scanner import Scanner
import serial
import time


scanner = Scanner(
    "/dev/ttyS0",
    baud_rate=9600,
    bytesize = serial.EIGHTBITS,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    timeout = 1
    )
scanner.open()

while True:
    try:
        data = scanner.read()
        print(data)
         
    except KeyboardInterrupt:
        scanner.close()
    time.sleep(1)