import socket


# AF_INET означает что мы будем использовать айпи протокол версии 4
# AF_INET6 означает что мы будем использовать айпи протокол версии 6
# AF_UNIX означает что мы будем использовать отдельный вид сокета по файлу
# SOCK_DGRAM означает что мы будем использовать протокол передачи данных UDP
# SOCK_STREAM означает что мы будем использовать протокол передачи данных TCP
# .recv метод приёма данных. Сокращенно от receive. Эта функция блокирует интерпритатор ожидая данные  # noqa
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


class TcpServerTest:
    """
    Server socket
    """
    def __init__(self):
        self.sock = None
        self.result = None
        self.count = 0
        self.client = None
        self.addr = None

    def open(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, host='127.0.0.1', port=8888):
        self.sock.bind((host, port))  # резервирование порта на нашей локальной машиине
        return True

    def listen(self, num=5):
        """
        каков размер очереди на сервер сокете. Тоесть количество клиентов которые подключатся и будут ожидать
        """
        self.sock.listen(num)
        return True

    def listen_many(self, size=1024, count=10):
        while True:
            try:
                self.client, self.addr = self.sock.accept()
            except Exception as e:
                print(f'Exception = {e}')
                break
            else:
                print('we in else')
                self.result = self.client.recv(size)
                print(f'{self.result = }')
                self.show_message()
        return True

    def show_message(self):
        print(f'Message = {self.result.decode("utf-8")}')
        print(f'Message size = {len(self.result.decode("utf-8"))}')
        return True

    def close(self):
        self.sock.close()
        return True


sock_obj = TcpServerTest()
with OpenSocket(sock_obj) as sock:
    sock.bind()
    sock.listen()
    sock.listen_many()
