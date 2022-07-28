# #Модуль содержит некоторые определенные функции и данные в отдельном файле
# # Допустим у нас есть модуль который содержится в файле my_module.py
#
# import my_module
#
# # И в нем есть некая функция foo()
#
# my_module.foo()
#
# # Или можно импортировать только одну функию из модуля
#
# from my_module import foo
# foo()
#
# # Или можно импортировать все функции из модуля
#
# from my_module import *
#
# foo()
#
# # Или можно импортировать функцию из модуля и дать ей другое имя у себя в проге
#
# from my_module import foo as my_foo
# my_foo() # Тоже самое что и foo()
#
# # Или
#
# import my_module as "Имя вместо my_module"
#
# import requests # Получает данные(какие-то) с сайтов
#
# first = 'https://stepic.org/media/attachments/course67/3.6.3/'
#
# last = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt').text
#
# r = ''
#
# while "we" not in r:
#
#     r = requests.get(first + last).text
#
#     last = r
#
#     counter += 1
#
# print(r)
#
# ### ПОЛЕЗНЫЕ МОДУЛИ НА ПЕРВОЕ ВРЕМЯ ДЛЯ НАЧАЛА
#
# from random import randint # randint(0, 10) функция выбирающая случайно число в указанном диапазоне в скобках
#
