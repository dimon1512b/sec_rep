
class Test:
    def __init__(self):
        print('we in init')
        self._first()

    def __first(self):
        print('we in first')


a = Test()
a.__first()
