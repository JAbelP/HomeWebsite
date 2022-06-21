import socket
import csv
import struct
import datetime

class MagicHomeApi:
    def __init__(self, device_ip, device_type, keep_alive=True):
        self.device_ip = device_ip
        self.device_type = device_type
        self.API_PORT = 5577
        self.latest_connection = datetime.datetime.now()
        self.keep_alive = keep_alive
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(3)
        try:
            print("Establishing connection with the device.")
            self.s.connect((self.device_ip, self.API_PORT))
        except socket.error as exc:
            print("Caught exception socket.error : %s" % exc)
            if self.s:
                self.s.close()

    def turn_on(self):
        """Turn a device on."""
        self.send_bytes(0x71, 0x23, 0x0F, 0xA3) if self.device_type < 4 else self.send_bytes(0xCC, 0x23, 0x33)
        
    def send_bytes(self, *bytes):
        """Send commands to the device.
        If the device hasn't been communicated to in 5 minutes, reestablish the
        connection.
        """
        check_connection_time = (datetime.datetime.now() -
                                 self.latest_connection).total_seconds()
        try:
            if check_connection_time >= 290:
                print("Connection timed out, reestablishing.")
                self.s.connect((self.device_ip, self.API_PORT))
            message_length = len(bytes)
            self.s.send(struct.pack("B"*message_length, *bytes))
            # Close the connection unless requested not to
            if self.keep_alive is False:
                self.s.close
        except socket.error as exc:
            print("Caught exception socket.error : %s" % exc)
            if self.s:
                self.s.close()