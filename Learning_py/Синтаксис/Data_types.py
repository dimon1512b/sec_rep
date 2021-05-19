'''Variable'''
# Переменный бывают приватными, тоесть использовать такие переменные или методы класса можно только в локальной среде
# этого же класса. Приватные переменные — это те переменные, которые видны и доступны только в пределах класса,
# которому они принадлежат.
class Mainclass:
    __private_variable = 2020;

    def __private_method(self):
        print("Это приватный метод")

    def insideclass(self):
        print("Приватная переменная:", Mainclass.__private_variable)
        self.__private_method()

foo = Mainclass()
foo.insideclass()
#>>> Приватная переменная: 2020
#>>>Это приватный метод
class Mainclass:
    __private_variable = 2020

    def __private_method(self):
        print("Это приватный метод")

    def insideclass(self):
        print("Приватная переменная:", Mainclass.__private_variable)
foo = Mainclass()
foo.insideclass()
foo.__private_method()
#>>>
#>>>AttributeError: ‘Mainclass’ object has no attribute ‘__private_method’



'''NUMBERS'''
# int - целочисленные
#1, 2, 3, 4, 5, 99...
# float - с плавающей точкой
#1.2, 2.3, 4.5, 6.7...
# Комплексные
#-5 + 4j, 2.3 - 4.6j
print( 10 / 3 )
#3.3333333333333335
print( 10 / 3.0 )
#3.3333333333333335
print(2**3)
#8
print(4**0.5) #извлечение корня квадратного
# 2
print(1+2)
#3
print(1.0+2)
#3.0

#С помощью функции round можно округлять числа до нужного количества знаков:
print(round(10/3.0,4))
#3.3333

#Остаток от деления:
print(10%3); a = 4 // 3; print(a); b = 10 // 3; print(b)
#1
#1
#3

#Конвертация через команды int, float, str,
a=11
print(float(a))
#11.0
print(10 == 10)
print(10 != 10)
#!= - не равно!
#True, False ( 0, 1 )
x1, x2, x3, = True, False, True
print(x1, x2, x3)
#True, False, True
print(x2 and x1)
#False
print(x1 or x2)
#True
print(not x1)
#False
#Приоритеты логических операций: 1) not x, 2) and, 3) or
x = 5
y = 10
#    10     25     10     10      5   10
#       False         True         True
print(y > x * x or y >= 2 * x and x < y)

'''О функции PRINT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print(something or *something, end= '' or sep= '')
#sep – разделяет объекты. Значение по умолчанию: ‘ ‘;
#end – ставится после всех объектов;

'''
'''STRINGS'''
intf = 'interface'
tun = 'Tunnel0'
print(intf + " " + tun)
#interface Tunnel0
print("Hello world")
#Hello world
print(intf * 5)
#interfaceinterfaceinterfaceinterfaceinterface
name = "Dimon"
print(name [0])
#D
#К функции ПРИНТ можно добавлять значения разделителя "print(1, 2, 3, sep=",") >>> 1,2,3
#Или print(123, end=" ")
#    print(321)
#    print(111)
#>>> 123 321
#    111
#Тоесть " end='' " указывает на то, что будет идти в конце принта и + прилепит после этого к себе следующий принт
# По умолчанию в конце принта стоит \n
'''СРЕЗЫ СТРОК'''
name = "Dimon"
print(name [2:4]) >>> #mo
print(name[1:-1]) >>> #imo
print(name[1:]) >>> #imon
print(name[-4:]) >>> #imon
print(name[:4]) >>> #Dimo
print(name[::-1]) >>> #nomiD
print(name[::-2]) >>> #nmD
print(name[0::2]) >>> #Dmn
print(name[0:-1:2]) >>> #Dm


# len подсчет количевства символов в строке
line = "interface Gi0/1"
line1 = [1, 2, 3.1, "dimon1512b"]
print(len(line))
#15
print(len(line1))
#4


'''Методы у строк'''

'1,2,3'.split(',')  # ['1', '2', '3']
'1,2,3'.split(',', maxsplit=1)  # ['1', '2,3']

'1,2,,3,'.split(',')  # ['1', '2', '', '3', '']
# сравните с '1 2   3'.split()

#Если разделитель не указан, разбиение пустой строки вернёт пустой список: [].

'1 2 3'.split()  # ['1', '2', '3']
'1 2 3'.split(maxsplit=1)  # ['1', '2 3']

'   1   2   3   '.split()  # ['1', '2', '3']
# сравните с '1,2,,3,'.split(',')


s = "aTGcc" p = "cc"

- s.upper() >>> "ATGCC"

- s.lower() >>> "atgcc"

- s.lst('p') >> > 1# сколько раз "р" встречается в "s"
- s.lst('o', 0, -1) # Другие два аргумента указывают диапазон поиска

- s.find('p') >>> 3# первое вхождение (индекс) р в s
              >>> -1 # значит что поиск не дал результатов
- s.find('p', 0, -1) # другие два аргумента указывают диапазон поиска
- s.rfind('o') >>> ... # Ищет первое вхождения елемента с правого конца
- s.find('A') >>> -1 # строка "А" не входит в s

a = '111'

- a.rjust(5, '-') >>> '--111' # Первый аргумент принимает значение ширины, второй принимает 1 символ
# которым будет заполнена недостача ширины
- a.ljust(7, '?') >>> '111????'

if "TG" in s:... >>> # Проверка вхождения в строку

- s.replace("c", "C") >>> "aTGCC" #Замением все вхождения "с" на "С", третий параметр указывает количевство замен

- s.isdigit() >>> True/False >>> # Состоит ли строка из одних лиш цифр

- s.isalpha() >>> True/False >>> # Состоит ли строка из одних лиш букв

#Функция и метод отличаются тем, что метод привязан к объекту конкретного типа, а функция, как правило,
#более универсальная и может применяться к объектам разного типа. Например, функция len может
#применяться к строкам, спискам, словарям и так далее, а метод startswith относится только к строкам.

'''LIST'''
#Список в Python это:
#последовательность элементов, разделенных между собой запятой и заключенных в квадратные скобки
#изменяемый упорядоченный тип данных
list1 = [10,20,30,77]
list2 = ['one', 'dog', 'seven']
list3 = [1, 20, 4.0, 'word']

#Функция list создает список
print(list("12345"))
#['1', '2', '3', '4', '5']
print(list("dimon"))
#['d', 'i', 'm', 'o', 'n']
line1 = list("Dimon1512b")
print(line1)
#['D', 'i', 'm', 'o', 'n', '1', '5', '1', '2', 'b']
line1[0] = "M"
print(line1)
#['M', 'i', 'm', 'o', 'n', '1', '5', '1', '2', 'b']

# Функия ''.join(list) вернет содержимое списка обратно в строку
A = ['red', 'green', 'blue']
print(' '.join(A)) #‘red green blue’
print(''.join(A)) #'redgreenblue'
print('***'.join(A)) #'red***green***blue'


'''Список в списке'''
list33 = [1, 2, 'd', (2j + 1), [1, 2, 3, "Вот он, 4 элемент под индексом 3 в встроенном списке списка \"line33\""]]
print(list33[4][3])
#Вот он, 4й элемент под индексом 3 в встроенном списке списка "line33"
#Со списками можно проводить математические операции используя математические операторы:
print(list33[4] * 2)
#[1, 2, 3, 'Вот он, 3 элемент под индексом 3 в встроенном списке списка "line33"',
# 1, 2, 3, 'Вот он, 3 элемент под индексом 3 в встроенном списке списка "line33"']
print(list33[4][0] * 2)
#2
print(list33[4][0] * 999)
#999
#Так как список - это упорядоченный тип данных, то, как и в строках,
#в списках можно обращаться к элементу по номеру, делать срезы:
print(list1[0])
#10
print(float(list1[0]))
#10.0
print(list3[::-1])

#Так как списки изменяемые, элементы списка можно менять:
list1 = [10,20,30,77]
list1[0] = 9
print(list1)
#[9, 20, 30, 77]

#Список в списке и обращение к элементам во вложеных списках
list4 = [[1,2,3], [4,5,6]]
print(list4[1][1])
#5
print(list4[0][1])
#2

#Sorted - эта функция создает новый список с отсортированными елементами исходного списка
b = [2, 1, 3, 4]
print(sorted(b))
#[1, 2, 3, 4]
c = ["Dimon", "Abraham", "Diman"]
print(sorted(c))
#['Abraham', 'Diman', 'Dimon']
b1 = sorted(b)
print(b1)
#[1, 2, 3, 4]
#Проверка пренадлежности элемента к списку:
Spisok = ["Dima", "Kolya", "Gena", "Анжелика", "Анжела", "Люда", "Тамара", "Марина", "Наташа", "Света", "Настя",/
"Валя", "Вера"]
if "Dima" in Spisok:
    print("Поздравляю" + " " + Spisok[0] + " " + "в списке!")
#Поздравляю Dima в списке!
#Задача! Пользователь вводит свое имя в строке, а программа должна проверить принадлежность его имени к списку и
#запрашевать у него повторный ввод в случае если его имени нету в списке или ввод был выполнен не правельно
while True:
    Name = input("Введите имя той женчины которую любит Дмитрий Юрьевич:")
    if Name == Spisok[3]:
        print("Эт правда)))")
        running = False
    elif Name in Spisok[4::]:
        print("Это его любовница, это не та самая женчина! Попробуйте ещё")
    else:
        print("Чет ты не так написала, попробуй ещё.")
else:
    print("Конец!")
'''Методы списков'''
# Метод .append() ==> spisok.append("Masha") - Добавляет елемент в список
# Метод .append() ==> spisok.append(["Masha", 'Helga']) - Добавляет список в список
# Метож .insert() ==> spisok.insert(1, "Olga") - Добавляет елемент в список на место указанного индекса со смещением
# в право всех остальных елементов
# Метод .remove() ==> spisok.remove("Masha") - Удаляет елемент из списка
# Метод .index() ==> spisok.index("Masha") - Возвращает индекс елемента в списке в виде целого числа
# Метод .sort() ==> spisok.sort() - Изменяет имеющийся список сортируя елементы в нем
# Метод .reverse() ==> spisok.reverse() - Изменяет имеющийся список меняя задом на перед елементы списка
# Конструкция del удаляет елемент из списка по индексу ==> del spisok[0]
# Конструкция min u max ==> min/max(spisok) - возвращает минимальное или максимальное значение списка
# Конструкция reversed() ==> reversed(spisok) - создает новый список на основании исходного с измененным порядком
# елементов сзоду на перед
# Генерация списков!!!
# a = [0] * 5 ==> [0, 0, 0, 0, 0]
# a = [0 for i in range(5)] ==> [0, 0, 0, 0, 0] - Выражение 0 каждый раз заменяет переменную i
# a = [i for i in range(5)] ==> [0, 1, 2, 3, 4] - Переменная i вместо выражения возвращает каждое значение i
# a = [i**2 for i in range(5)] ==> [0, 1, 4, 9, 16] - Указали переменную в квадрате
# Функция sum() ==> sum(spisok) - Возвращает сумму елементов списка INT
''' ГЕНЕРАЦИЯ ДВОХМЕРНЫХ СПИСКОВ!!!'''
'''Кортеж. Похож на список. Содержит значения через заяпяту. Не изменяем. Круглые скобки'''

a = tuple() # Create new tuple
a = tuple('hello, world!')
#>>> a
#('h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!')
'''Кортеж поддерживает:'''
# - Операторы среза
# - Доступ по индексу
# - Кортеж можно умножить на целое число и он умножит значения внутри себя
# - Кортеж можно сложить с дргуим кортежем и получиться один. Первыми будут элементы из кортежа который
# в сложении стоит первым
# - Кортежи можно использовать в качестве ключей словаря в отличии от списков
# - Можно кортеж превратить в список с помощью функции list и наооборот
# - Все методы списка типо count которые не изменяют его
# - Можно менять местами кортежи
# -



'''DICTIONARY - СЛОВАРЬ'''
#данные в словаре - это пары ключ: значение
#доступ к значениям осуществляется по ключу, а не по номеру, как в списках
#данные в словаре упорядочены по порядку добавления элементов
#так как словари изменяемы, то элементы словаря можно менять, добавлять, удалять
#ключ должен быть объектом неизменяемого типа: число, строка, кортеж
#значение может быть данными любого типа
