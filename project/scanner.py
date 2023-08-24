import serial



class Scanner:
    def __init__(
        self,
        urt_port: str,
        baud_rate: int = 9600,
        bytesize = serial.EIGHTBITS,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        timeout = 1
        ) -> None:
        """
            Initialize a Scanner instance.

        Args:
            urt_port (str): The name of the serial port
            baud_rate (int): The baud rate for serial communication. Defaults to 9600.
        """
        self.urt_port = urt_port
        self.baud_rate = baud_rate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        self.serial_connection = None
        
    def open(self) -> None:
        try:
            self.serial_connection = serial.Serial(
                port = self.urt_port,
                baudrate = self.baud_rate,
                bytesize = self.bytesize,
                parity = self.parity,
                stopbits = self.stopbits,
                timeout = self.timeout
            )
            print(f"serial port {self.urt_port} is open with {self.baud_rate} baud .")
        except serial.SerialException as e:
            print(f"Error : {e}")
            
    def read(self) -> str:
        if self.serial_connection:
            try:
                data = self.serial_connection.read().decode()
                if data:
                    return data
            except serial.SerialException as e:
                print(f"Error while reading data {e}")
    
    def close(self) -> None:
        if self.serial_connection:
            self.serial_connection.close()
            print(f"Serial port {self.urt_port} closed .")
                