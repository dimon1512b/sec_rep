"""Декораторы"""


def decator1(func):
    def inner():
        print('Start')
        func()
        print('Finish')

    return inner


def say1():
    print('Hello World!')


d = decator1(say1)
d()
# Но чтобы разширить функционал функции say до того что мы сейчас сделали нужно задекорировать её след образом

say1 = decator1(say1)  # ДЕкорируем её

say1()  # Сдесь она уже делает d = decator1(say1) d()  вот эти вещи

"""Но чтобы say могла принимать больше аргументов их нужно описать в самом декораторе через *args, **kwargs"""


def decator(func):
    def inner(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('Finish')

    return inner


def say(name, surname, age):
    print('Hello!', name, surname, age)


say = decator(say)

say('vasya', 'ivanov', 23)  # >>> Start


# >>> Hello! vasya ivanov 23
# >>> Finish


# Можно добавить уровни дикорирования функции

def header(func):  # Просто создали ещё одно замыкание
    def inner(*args, **kwargs):
        print('h1')
        func(*args, **kwargs)
        print('/h1')

    return inner

def table(func):  # Просто создали и ещё одно замыкание
    def inner(*args, **kwargs):
        print('table')
        func(*args, **kwargs)
        print('/table')

    return inner

def hello(name):
    print('Hello', name)
hello = header(table(hello))
hello('Vasya')

# Но все это пишеться короче если использовать оператор дикорирования @

#def header(func):  # Просто создали ещё одно замыкание
#    def inner(*args, **kwargs):
#        print('h1')
#        func(*args, **kwargs)
#        print('/h1')
#
#    return inner
#
#def table(func):  # Просто создали и ещё одно замыкание
#    def inner(*args, **kwargs):
#        print('table')
#        func(*args, **kwargs)
#        print('/table')
#
#    return inner
#@header
#@table >>> #  hello = header(table(hello)) # Называется навешеванием декораторов
#def hello(name):
#    print('Hello', name)
#
#hello('Vasya')
from _datetime import datetime

def decor_time(func):
    def inner():
        start = datetime.now()
        func()
        finish_time = datetime.now() - start
        print(finish_time)
    return inner
@decor_time
def lst_com():
    lst = [i for i in range(10**7) if i%2 == 0]
@decor_time
def for_lst():
    lst = []
    for i in range(10**7):
        if i%2 == 0:
            lst.append(i)
lst_com()
for_lst()

"""Чтобы не потерять имя и документацию функции __name__ and __doc__ после дикорирования нужно в дикораторе
 их переопределить"""
def table2(func): #новый декоратор
    def inner(*agrs, **kwargs):
        print('table2')
        print(func(*agrs, **kwargs))
        print('table2')
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
@table2 # задекорировали нашу функцию - это раносильно sqr = table2(sqr)
def sqr(x):
    '''
    Возводим х в квадрат
    :param x: любое число
    :return: x**2
    '''
    return x ** 2
sqr(2) #table2
       #4
       #table2

print(sqr.__name__) # >>> sqr
print(sqr.__doc__)  # Возводим х в квадрат
                    #:param x: любое число
                    #:return: x**2

'''Или можем задекорировать наш inner через импортированный декоратор wraps from functools import wraps
@wraps(func) func это та функция имя и доки которой мы хотим сохранить'''


'''Property - Можно задекорировать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
class A():
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    @property
    def my_balance(self):
        print('Сработал метод Гет')
        return self.__balance
    @my_balance.setter
    def my_balance(self, value):
        print('Сработал метод Сет')
        self.__balance = value
    @my_balance.deleter
    def my_balance(self):
        print('Сработал метод ДЕЛ')
        del self.__balance
exemp1 = A('Ivan', 200)
exemp1.my_balance #>>> Will be getter
exemp1.my_balance = #n# >>> Will be setter
#del exemp1.my_balance >>> Will be deleter

'''staticmethod and classmethod '''

class Example:
    def hello():
        print('Hello') # >>> Example.hello() воспринимается как функция и готова к работе через класс

    def instance_hello(self):
        print(f'instance_hello {self}') # >>> ex1.instance_hello() вопринимается как метод и обезательно принимает селф
                                        # тоесть от класса его вызвать нельзя
    @staticmethod # Нужен когда хочеться создать функцию и не выносить её вне класса, а оставить в классе
    def static_hello():
        print('static_hello') # >>> Вызывается как от екземпляра так от класса

    @classmethod # Нужен когда хочеться сделать какуюто обработку не над экземпляром на над классом
    def class_hello(cls):
        print(f'class_hello {cls}') # >>> Вызывается от класса и принимает в качевстве аргумента сам класс
                                    # >>> Даже если вызвать от экземпляра то в аргумент всеравно прилетит сам класс

