import socket
import sys
import time


class OpenSocket:
    def __init__(self, host='localhost', port=8888):
        self.sock = TcpClientTest()
        self.host = host
        self.port = port

    def __enter__(self):
        self.sock.connect(self.host, self.port)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        return True


class TcpClientTest:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host='127.0.0.1', port=8888):
        self.sock.connect((host, port))

    def send(self, message=b'Test message'):
        self.sock.send(message)
        return True

    def close(self):
        self.sock.close()
        return True


input_message = str(sys.argv[1]).encode() if len(sys.argv) > 1 else b'Empty input'
with OpenSocket() as sock_client:
    sock_client.send(message=input_message)
