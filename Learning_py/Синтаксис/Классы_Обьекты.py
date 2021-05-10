# Класс - инструкция по которой создается обьект. Чертеж
# На основании класса создается обьект или так называемый экземпляр.
# Классы могут взаемодействовать друг с другом
# Обьект по инструкции назывется экземпляр класса
# Классы можно импортировать в виде модулей ''' from Modul import Something_Class, Or_another_Class '''
# дальше работаем свободно с экземплярами
# Или импортируем полностью модуль ''' import module ''' >>> a4 = module.Class(arguments)
# Или импортируем весь модуль с использованием "*" ''' from module import * ''' >>> a4 = Class(arguments)

'''Атрибуты класса'''


class Person():
	name = 'Ivan'  # Атрибут
	age = 30  # Атрибут


# Для обращения к атрибутам нужно Person.atriboot
# Или через функцию getattr(Class, 'atriboot', value_atriboot) получаем значение атрибута. Но если атрибута нет
# то возвращает указаное по умолчанию значение

# Значение атрибута можно менять
# Атрибут и его значение можно создать через оператор присваевания
Person.x = 100  # Создает атрибут или меняет значение имеющегося
# Можно использовать функцию setattr(Class, 'attr', value_attr) меняет значение или создает атрибут
setattr(Person, 'y', 200)  # Созздан атрибут

# Можно удалить атрибут

del Person.x  # Здесь атрибут удален

# или функция delattr(Class, 'attr')
delattr(Person, 'y')  # Сдесь атрибут удален

# Изминение атрибутов класса прямопропорционально влияет на атрибуты экземпляров. Но озминение атрибутов
# у самых экземпляров не влияет на атрибуты других экземпляров

'''Атрибуты экземпляра класса'''

# При создании экземпляра класса "ex = Class()" он принимает в себя все атрибуты класса но может иметь и свои личные
# Созздать атрибут для экземпляра можно так "ex.atr = volue" а проверить так "ex.__dict__ >>> {atr : volue}"
# Созданный атрибут внутри экземпляра никак не сказывается на атрибуты внутри класса
# Даже если удалить атрибут у экземпляра то это не повлияет на атрибуты класса
# Обращаясь к атрибуту экземпляра поиск происходит в первую очередь в пространстве имен этого экземпляра
# а если такой атрибут не нашелся то поиск происходит в пространстве имен класса

'''Функции как атрибут класса'''


class Car:
	model = 'BMW'
	engine = 1.6

	@staticmethod  # Это нужно чтобы можно было не указывать Self в аргументы функции
	def drive():
		print('Let\'s go')


# Вызов функции:
Car.drive()  # Для класса это ФУНКЦИЯ

getattr(Car, 'drive')()

a1 = Car()

a1.drive()  # Для экземпляра класса это МЕТОД

'''self должен быть всегда в скобках аргументов метода'''


class Cat():
	def name_of_cat(self, name, age=0):
		self.name = name
		self.age = age
		print(self.name, self.age)


cat1 = Cat()
cat1.name_of_cat('Harry', 15)  # >>> Harry 15

'''__init__ - магический метод. Два нижних поччеркиваний с обеих сторон обязательны
Метод срабатывает автоматически после создания обьекта, тоесть экземпляра класа 
Метод нужен для инициализации, тоесть для заполнения нашего обьекта какими либо значениями'''


class Cat():
	def __init__(self, name, age=0, color='black'):
		self.name = name
		self.age = age
		self.color = color
		print('Hello new object', self)


tom = Cat('Tom', 15, 'Black')  # >>> Hello new object <__main__.Cat object at 0x000001C2D4D3A670>
print(tom)  # >>> <__main__.Cat object at 0x000001B303CFA670>

scott = Cat('Scott', color='white')  # Сдесь создался экземпляр красса имеющий свои атрибуты

'''Принцип написания кода Dry, это описание метода класса укороченным путем через использование уже имеющегося метода
DON'T REPEAT YOURSELF '''
'''Принцип единой отведственности это когда функция отвечает за конкретный функционал в которой описан именно целевой
код приследующий одну цель'''


class Point:
	def __init__(self, x=0, y=0):
		self.move_to(x, y)  # Используем имещийся метод чтобы не повторять строчки

	def move_to(self, new_x, new_y):
		self.x = new_x
		self.y = new_y

	def go_home(self):
		self.move_to(0, 0)  # Используем имещийся метод чтобы не повторять строчки


p1 = Point(3, 4)
p2 = Point(-54, 32)
p3 = Point()
p3.move_to(4, 5)

'''КАК ПОЛУЧИТЬ ЗНАЧЕНИЕ АТРИБУТА ЭКЗЕМПЛЯРА КЛАССА'''


class Lamp:
	def __init__(self, floor=0, color='yellow', power=60):
		self.floor = floor
		self.color = color
		self.status = False
		self.power = power


ex1 = Lamp()
print(getattr(ex1, 'power'))
# OR
print(ex1.color)  # >>> yellow

''' КАК ИЗМЕНИТЬ ЗНАЧЕНИЕ АТРИБУТА У ВСЕХ ЭКЗЕМПЛЯРОВ. ИМЕЕТСЯ В ВИДУ ОДИН ОБЩИЙ АТРИБУТ КОТОРЫЙ ИМЕЕТСЯ У 
ВСЕХ ЭКЗЕМПЛЯРОВ
ЭТО НАЗЫВАЕТСЯ МОНОСОСТОЯНИЕМ ЭКЗЕМПЛЯРОВ КЛАССА'''


class Caat:
	__shared_attr = {
		# Создаем словарь на который будут ссылаться все экземпляры класса для определения своих атрибутов
		'breed': 'pers',
		'color': 'black'
	}

	def __init__(self):  # Инициализируем атрибуты всех экземпляров ссылаясь на приватный изменяемый словарь
		self.__dict__ = Caat.__shared_attr


# Теперь при создании каждого экземпляра им будут присваиваться одинаковые атрибуты из словаря на
# который мы ссылаемся


a = Caat()
b = Caat()  # Здесь их атрибуты одинаковы
a.breed = 'siam'  # Здесь мы изменяя значение атрибута у одного экземпляра, изменяем это значение у самого словаря
# на который ссылаються все экземпляры инициализируя свои атрибуты, следовательно b.breed будет также изменен
# ЭТО НАЗЫВАЕТСЯ ПОВЕДЕНИЕМ МОНОСОСТОЯНИЯ
print(b.breed)  # >>> siam

'''Property - свойство атрибута экземпляра!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


class Bank():
	def __init__(self, name, balance):
		self.name = name
		self.__balance = balance

	def get_balance(self):
		return self.__balance

	def set_balance(self, item):
		if not isinstance(item, (int, float)):
			raise ValueError('Баланс должен быть числом')
		else:
			self.__balance = item

	def del_balance(self):
		del self.__balance

	balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)


a = Bank('Ivan', 100)
print(a.get_balance())  # >>> Можно получить баланс но это не удобно
print(a.set_balance(3))  # >>> Можно установить баланс но это не удобно
print(a.balance)  # >>> Просто и прямо получаем значение баланса
a.balance = 200  # >>> Просто и прямо устанавливаем значение баланса
del a.balance  # >>> Просто и прямо удаляем атрибут экземпляра класса баланса

'''Property - Можно задекорировать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


# Для этого Геттеры и Сеттеры должны быть одним именем
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
# xemp1.my_balance #>>> Will be getter
# exemp1.my_balance = #n# >>> Will be setter
# del exemp1.my_balance >>> Will be deleter


'''__str__ and __repr__!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


# метод __str__ срабатывает автоматически при
# метод __str__ будет отвечать за то как наш обьект будет отображен в члучаее если к нему применить такие функции
# str or print или он отвечает за то как увидит этот обьект пользователь
# метод __repr__ будет отвечать за то как наш экземпляр класса будет отображаться внутри нашей системы то есть
# как её будут видеть разработчики
# В случаее если применяются оба эти метода, то всюду идет отоюражение как указано в __str__
class Lion():
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'The object Lion - {self.name}'

	def __str__(self):
		return f'The Lion - {self.name}'


simba = Lion('Simba')
print(simba)  # >>> The Lion - Simba


class Money():
	def __init__(self, dollars, cents):
		self.total_cents = dollars * 100 + cents

	def __str__(self):
		return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"

	@property
	def dollars(self):
		return self.total_cents // 100

	@dollars.setter
	def dollars(self, value):
		if isinstance(value, int) and value >= 0:
			self.total_cents = (self.total_cents % 100) + value * 100
		else:
			print("Error dollars")

	@dollars.deleter
	def dollars(self):
		del self.dollars

	@property
	def cents(self):
		return self.total_cents % 100

	@cents.setter
	def cents(self, value):
		if isinstance(value, int) and value < 100 and value >= 0:
			self.total_cents = (self.total_cents // 100) * 100 + value
		else:
			print("Error cents")

	@cents.deleter
	def cents(self):
		del self.cents


client = Money(101, 99)

client.dollars = 2009

client.cents = 99

print(client)

'''Исчисляемые Property!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


class Per():
	def __init__(self, side):
		self.__side = side
		self.__per = None

	@property
	def side(self):
		return self.__side

	@side.setter
	def side(self, value):
		self.__side = value
		self.__per = None

	@property
	def per(self):
		if self.__per is None:
			self.__per = self.__side * 4
		return self.__per


a = Per(5)

a.side = 10

print(a.per)

'''Пространство имен класса!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


# в него входят:
# атрибуты класса
# названия методов
# методы в классах не увидят PYTHON_DEV если обратится к переменным на прямую. Развечто этот PYTHON_DEV будет находиться
# в глобальной области видимости. Но получить значния этих переменных можно через экземпляр класса (self) или сам класс

class DepartmentIT():
	PYTHON_DEV = 3
	GO_DEV = 3
	REACT_DEV = 2

	def make_backend(self):
		print(it1.PYTHON_DEV or DepartmentIT.PYTHON_DEV)

	def make_frontend(self):
		print('React')


it1 = DepartmentIT()

'''__abs__ and __len__!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


class Otrezok():
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def __len__(self):  # длинна отрезка
		return abs(self.p2 - self.p1)

	def __abs__(self):
		return abs(self.p2 - self.p1)


q = Otrezok(2, 5)

print(len(q))

"""Также работают и методы  __add__(сложение), __mul__(умножение), __sub__(вычитание) и __truediv__(деление)"""


class Otrezok2():
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2

	def __len__(self):  # длинна отрезка
		return abs(self.p2 - self.p1)

	def __abs__(self):
		return abs(self.p2 - self.p1)

	def __add__(self, other):
		if isinstance(other, Otrezok2):
			self.p1 += other.p1
			self.p2 += other.p2


w = Otrezok2(5, 2)  # len = 3

r = Otrezok2(9, 2)  # len = 7

r + w  # мне кажеться что это странно
print(len(w), len(r))  # 3 and 7+3=10

"""Магические методы"""

import math


class Vector2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return 'Vector2D({}, {})'.format(self.x, self.y)

	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

	def __add__(self, other):
		return Vector2D(self.x + other.x, self.y + other.y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

	def __sub__(self, other):
		return Vector2D(self.x - other.x, self.y - other.y)

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self

	def __abs__(self):
		return math.hypot(self.x, self.y)

	def __bool__(self):
		return self.x != 0 or self.y != 0

	def __neg__(self):
		return Vector2D(-self.x, -self.y)


class Counter:
	def __init__(self):
		self.counter = 0
		self.summa = 0
		self.lenght = 0

	def __call__(self, *args, **kwargs):  # Делает экземпляр класса вызывающимся
		self.counter += 1
		self.summa += sum(args)  # args хранит в себе tuple
		self.lenght += len(args)
		print(f'наш экземпляр вызывался {self.counter} раз')


"""Декорируем __call__"""

from time import perf_counter


class Timer:
	def __init__(self, func):
		self.fn = func

	def __call__(self, *args, **kwargs):
		start = perf_counter()
		print(f'вызывается функция {self.fn.__name__}')
		result = self.fn(*args, **kwargs)
		finish = perf_counter()
		print(f'функция отработала за {start - finish}')
		return result


@Timer
def fact(n):
	pr = 1
	for i in range(1, n + 1):
		pr *= i
	return pr


def fib(n):
	if n <= 2:
		return 1
	return fib(n - 1) + fib(n - 2)


print(fact(6))

print(Timer(fib)(20))

"""Полиморфизм как принцип ООП"""


# Заключается в том чтобы одна функция или обьект имел разное поведение автоматически
# Например

class Rectangle:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return f'Прямогульник со сторонами {self.a}x{self.b}'

	def get_area(self):
		return self.a * self.b


class Square:
	def __init__(self, a):
		self.a = a

	def __str__(self):
		return f'Квадрат со сторонами {self.a}x{self.a}'

	def get_area(self):
		return self.a * self.a


class Circle:
	def __init__(self, r):
		self.r = r

	def __str__(self):
		return f'Круг с радиусом {self.r}'

	def get_area(self):
		return 3.14 * self.r


rec1 = Rectangle(3, 4)  # Создан экземпляр класса

sq1 = Square(5)  # Создан экземпляр класса

cir1 = Circle(5)  # Создан экземпляр класса

figures = [rec1, sq1, cir1]  # Создан список содержащий экземпляры классов

for figure in figures:  # Проходимся по экземплярам

	print(figure)  # Одной полиморфической фразой вызываем разное поведение для обьектов
	# Прямогульник со сторонами 3x4
	# Квадрат со сторонами 5x5
	# Круг с радиусом 5
	print(figure.get_area())  # Одной полиморфической функцией вызываем разное поведение для обьектов
# 12
# 25
# 15.700000000000001

'''__getitem__ __setitem__ __delitem__ Нужны для того чтобы обращатся к обьектам по индексам'''


class Vector99:
	def __init__(self, *args):
		self.values = list(args)

	def __repr__(self):
		return str(self.values)

	def __getitem__(self, item):
		return self.values[item]

	def __setitem__(self, key, value):
		if key >= len(self.values):  #
			diff = key - len(
				self.values) + 1  # Определяем разницу чтобы знать сколько нужно добавить элементов в список
			self.values.extend(
				[0] * diff)  # Метод "extend" заполняет недостающие елементы в колекции указанным значением
			self.values[key] = value  # Сдесь когда уже список расширен, то добавляем необходимое значение на key
		else:
			self.values[key] = value

	def __delitem__(self, key):
		del self.values[key]


v1 = Vector99(1, 2, 2, 444)

v1  # [1, 2, 2, 444]

v1[0] = 5

'''__iter__ делает указанный обьект итерабельным, __next__ указывает на поведение итерации'''

'''НАСЛЕДОВАНИЕ!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''

'''ЗА ОСНОВУ БЕРЕМ РОДИТЕЛЬСКИЙ КЛАСС И МОЖЕМ ДОБАВЛЯТЬ НОВЫЕ МЕТОДЫ И ФУНКЦИИ К ДОЧЕРНЕМУ КЛАССУ'''
'''Те атрибуты или методы которые должны быть во многих классах лучше вынести в родительский отдельный класс
После этого достаточно только в скобках названия дочернего класса при его создании указать родительский'''
'''ЭКЗЕМПЛЯРЫ КЛАСА МОГУТ БЫТЬ ЗНАЧЕНИЯМИ АТРБУТОВ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


class Roditelskiy:
	def can_walk(self):
		print('I can walk')


class Doctor(Roditelskiy):

	def can_cure(self):
		print('I can cure')


class Architect(Roditelskiy):

	def can_build(self):
		print('I can build')


d = Doctor()
d.can_cure()

a = Architect()
a.can_build()

d.can_walk()

a.can_walk()

# функция issubclass(classSub, classParent) помогает определить является ли клас подклассом ==> bool
print(issubclass(Doctor, Roditelskiy))  # ==> True


# экземпляры подкласса обретают пренадлежность к родителькому классу тоже.
# Родительский класс также получает и атрибуты и методы подкласов но подкласс из другой цепочки не получает поведения из
# родительского класса которое пришло в него с третьего подкласса

# Даже если создать подкласс от подкласса то самый нижний подкласс всеравно получит поведение Родительского класса
# Если они находяться на одной цепочке наследования


class Vehicle(): pass


class Car(Vehicle): pass


class RaceCar(Car): pass


class Plane(Vehicle): pass


class Boat(Vehicle): pass


# Если мы не указали обьект от которого будет наследоваться класс, то по умолчанию он будет наследваться он object
# Так как все в питоне является обьектом
# Object по сути является родительским классом всего
'''Переопридиление методов родительского класа, путем присвоения дочернему классу атрибутов и методов
с таким же названием но разным поведением!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''


class Person:
	def breathe(self):
		print('Человек Дышит')

	def walk(self):
		print("Человек Ходит")


class Doctor(Person):
	pass


a = Person()

b = Doctor()

a.breathe()  # >>> 'Человек Дышит'
b.breathe()  # >>> 'Человек Дышит'
# Это происходит потому что класс Доктор не найдя у себя необходимых методов, обратился за ними в родительский клас

# Но это поведение можно переопределить если в дочернем классе определить функцию с таким же названием но задав ей
# другое поведение

# Точно так же это работает в случае с атрибутами

# Точно так же это работает в случае с магическими методами

'''Extending - расширение дочернего класса путем присвоения ему новых методов и атрибутов'''
'''Делегирование - как концепция наследования'''


# Функция super().method() обращается к родительскому классу и вызывает указанную функция в родительском классе

class Delegirovanie():
	def __init__(self, del1, del2):
		self.del1 = del1
		self.del2 = del2


class Sub_Delegirovanie(Delegirovanie):
	def __init__(self, del1, del2, del3):
		super().__init__(del1, del2)  # Что б не повторять код, берем его из родительского класса
		self.del3 = del3  # А чево не хватило в родительком классе дописываем сдесь


de = Delegirovanie(1, 2)

s_de = Sub_Delegirovanie(1, 2, 3)

'''Множественное наследование. Порядок важен'''


class Rod1():  # Создали первого родителя
	atr1 = 0


class Rod2():  # Создали второго родителя
	atr1 = 1


class Sub(Rod1, Rod2):  # Создали наследника
	def atr(self):
		print(self.atr1)


a = Sub()

a.atr()  # >>> Это будет именно 0 потому что программа не найдя этого атрибута у
# нашего класса наследника, будет искать его
# сначала в том родительском классе который в скобках наследования указа первым


'''Slots'''


# У экземпляра класса будут только те атрибуты которые указаны в переменной __slots__.
# Также у такого экземпляра пропадает метод __dict__
class Pooint():
	__slots__ = ('x', 'y')  # Нужно передавать именно массив. Но это не точно

	def __init__(self, x, y):
		self.x = x
		self.y = y


# Первое преимущество использования Слотов. Ограничивается количевство атрибутов
# Второе. Атрибуты занимают меньше памяти
# Третье. Операции над атрибутами производятся быстрее на 30%

'''Slots вместе с свойствами и наследованием'''


class Rectangle:
	__slots__ = ('width', 'height')

	def __init__(self, width, height):
		self.height = height
		self.width = width

	@property
	def perimetr(self):
		return (self.height + self.height) * 2

	@property
	def aria(self):
		return self.height * self.height


ar = Rectangle(3, 4)  # Инициализированы атрибуты 3 и 4 но больше атрибутов быть не может


class Square(Rectangle):
	# Если не указывать в дочерем классе Слотс то он и не будет им ограничен. Тоесть можно будет создавать
	# новые атрибуты и __dict__ будет доступен
	__slots__ = 'color'  # Создавая слотс в дочернем классе мы также получаем те переменные которые хранятся в слотс

	# родительского класса
	def __init__(self, width, height, color):
		super().__init__('width', 'height')
		self.color = color


'''Exception - исключения'''

# Исключения бывают двух типов. 1. Те которые появляються в момент выполнения программы. 2. Те которые появляються до
# начала выполнения программы, так называемые ошибки кампиляции
try:
	# code
	pass
except ValueError:  # TypeError
	# Что делать в случае пойманой ошибки
	pass

'''У типов исключений есть ветка наследования. Так как все они представляют из себя классы. Указывая в Exception 
родительский класс исключения можно отлавливать все его дочерние исключения'''


def first():
	print('Start')
	print('Finish')


# Обработка исключений
# Как только в блоке try находится искомая ошибка, то все что было ниже в этом блоке выполнятся не будет
try:
	int('abc')
	1 / 0
	[][2]
except ValueError:
	print('ValueError')
# ==> ValueError. Потому что найдя исключение в блоке try происходит что-то типо break.
# Но если поставить первой строчкой в блоке Трай деление на 0 то вылезет ошибка Деления на 0 так как эту ошибку мы не
# указали что отлавливаем
# Для того чтобы обработать ошибку деления на 0 то нужно добавить ещё один Ексцепт
try:
	int('abc')
	1 / 0
	[][2]
except ValueError:
	print('ValueError')
except ZeroDivisionError:
	print('ZeroDivisionError')
# И когда программа в блоке Трай найдет первую из искаемых ошибок то сработает по типу оператора Брейк

# Не указывая никакой тип ошибки мы отлавиваем все типы исключений

try:
	1 / 0
except:
	print('error')
# ==> error

# Но в таком случае лучше использовать except Exception:

# Блок finally будет отрабатывать в любом случае
try:
	1 / 0
except (TypeError, ZeroDivisionError):  # В масссиве через запятую можно указывать несколько типов отлавливаемых ошибок
	print('error')
finally:
	print('end')

# Если мы обрабатываем какое-то исключение описанное в Екцепт то можем написать оператор Елс который отрабатает в том
# случае когда не будет найдено ни одно исключение

try:
	1 / 5
except:
	print('error')
else:
	print('all right')

''' raise - возбуждает исключения'''
# raise TypeError('Text error') - эта конструкция позволяет самому вызывать исключения

''' Custom Exception - Пользовательские исключения'''


# Для того чтобы создать пользовательское исключение нужно создать класс наследованный от Exception

class My_Exception():
	'''This is my first Exception'''

# Следовательно это исключение можно использовать в конструкции Трай или Рейз
