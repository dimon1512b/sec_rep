import socket
import sys


class UdpClientTest:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_to(self, host='127.0.0.1', port=8888, message=b'Test message'):
        self.sock.sendto(message, (host, port))
        return True


input_message = str(sys.argv[1]).encode() if len(sys.argv) > 1 else b'Empty input'
sock_client = UdpClientTest()
sock_client.send_to(message=input_message)
