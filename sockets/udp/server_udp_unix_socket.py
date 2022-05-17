import os
import socket

# AF_INET означает что мы будем использовать айпи протокол версии 4
# AF_INET6 означает что мы будем использовать айпи протокол версии 6
# AF_UNIX означает что мы будем использовать отдельный вид сокета по файлу
# SOCK_DGRAM означает что мы будем использовать протокол передачи данных UDP
# .recv метод приёма данных. Сокращенно от receive. Эта функция блокирует интерпритатор ожидая данные
import time


class OpenSocket:
    def __init__(self, sock_to_open):
        self.sock = sock_to_open

    def __enter__(self):
        self.sock.open()
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        return True


class UdpServerTest:
    """
    Server socket
    """
    def __init__(self):
        self.sock = None
        self.result = None
        self.count = 0

    def open(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    def bind(self, file='unix.sock'):
        if os.path.exists(file):
            os.remove(file)
        self.sock.bind(file)  # резервирование файла
        return True

    def listen_one(self, size=1024):
        self.result = self.sock.recv(size)  # размер байт
        self.show_message()
        return True

    def listen_many(self, size=1024, count=10):
        while self.count < count:
            self.count += 1
            self.result = self.sock.recv(size)
            self.show_message()
        return True

    def show_message(self):
        print(f'Message = {self.result.decode("utf-8")}')
        print(f'Message size = {len(self.result.decode("utf-8"))}')
        return True

    def close(self):
        for i in range(0):
            time.sleep(10)
            print((i + 1) * 10)
        self.sock.close()
        return True


sock_obj = UdpServerTest()
with OpenSocket(sock_obj) as sock:
    sock_file_name = '../unix_test.sock'
    sock.bind(sock_file_name)
    sock.listen_many()
