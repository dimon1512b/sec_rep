# Функция min4 в качестве параметров принимает 4 значения
def min4(a, b, c, d = 10):
  if a <= b and a <= c and a <= d:
    return a
  elif b <= a and b <= c and b <= d:
    return b
  elif c <= a and c <= b and c <= d:
    return c
  else:
    return d
print(min4(11, 22, 11, 9))
# Функция может не принимать никаких значений
def a():
  return x + y
x = 1
y = 2
print(a())
# Функция может принимать произвольное число параметров
def min(*a):
  m = a[0]
  for x in a:
    if m > x:
      m = x
  return m
print(min(1, 2, 3, 4, 5, 0))
#Функиция может принимать значения параметров по умолчанию
def my_range(start, stop, step = 1):
  res = []
  x = start
  if stop == start:
      return [start]
  if step > 0:
    if stop < start:
        return '''something wrong
stop < start'''
    while x < stop:
      res.append(x)
      x += step
  elif step < 0:
    if start < stop:
        return """Wrong!!!
start < stop"""
    while x > stop:
      res.append(x)
      x += step
  return res
print(my_range(1, 10))
# ЛОКАЛЬНЫЕ ПЕРЕМЕННЫЕ МОЖНО ИСПОЛЬЗОВАТЬ ТОЛЬКО ВНУТРИ ФУНКЦИИ
def init_values():
  a = 100
  b = 200
init_values()
#print(a + b) # NameError: name 'b' is not defined
a = 0
print(a) # 0
def init_values(a):
  a = 5
b = 10
init_values(b)

print(b) # 10

def append_zero(xs):
  xs.append(0)
  xs = [100]
list = []
append_zero(list)
print(list) # [0]
# Глобальные переменные
def print_value():
  print(a)
a = 5
print_value() # 5

# Так нельзя!

def print_value2():
  print(a)
  a = 10
  print(a)
a = 5
print_value2() # UnboundLocalError: local variable 'a' referenced before


# ФУНКЦИЯ ПРИ ВЫЗОВЕ КОТОРОЙ ИЗМЕНЯЕТСЯ ИМЕЮЩИЙСЯ СПИСОК

import random


list = [random.randint(0, 20) for i in range(random.randint(0,10))]
print(list)
def modify_list(l):
  ll = len(l)
  x = 0
  while x != ll:
    if l[x] % 2 == 0:
      l[x] = l[x] // 2
      x += 1
    else:
      l.remove(l[x])
      ll -= 1


modify_list(list)

# Используя лист компрехеншн можно написать тоже самое на 2 строчки...
def modify_list(l):
  l[:] = [i // 2 for i in l if i % 2 == 0]

"""Если в теле функции нету Ретёрн то функция будет возвращать значение Нон"""

"""Замыкания"""

def main_func(value):
  name = value
  def in_func():
    print('Hello my friend', name)
  return in_func

z = main_func('Misha')
print(type(z)) # >>> z is function
z() # >>> Hello my friend Misha
y = main_func('Ivan')
y() # >>> Hello my friend Ivan
# Получается что у функции z and y разные name

def adder(value):
  def inner(a):
    return value + a
  return inner
a2 = adder(2) # >>> <function adder.<locals>.inner at 0x000001409C2DD550>
print(a2(10)) # a2 имеет области видимости value = 2. А при вызове самой функции а2, мы передаем значение для вложенной
#функции


def counter():
  count = 0
  def inner():
    nonlocal count
    count += 1
    return count
  return inner
q = counter()# Присваеваем переменной значение функции и при каждом новом вызове будет показано
# сколько раз было вызвана эта функция ранее
print(q())   #1
print(q())   #2
print(q())   #3
print(q())   #4
print(q())   #5
print(q())   #6
print(q())   #7
print(q())   #8
print(q())   #9
r = counter()# Новая переменная значит новая область видимости и новый счетчик
print(r())   #1
print(r())   #2
print(r())   #3
print(r())   #4
print(r())   #5
print(r())   #6
print(r())   #7
print(r())   #8
print(r())   #9


"""Декораторы@@@@@"""

def decator(func):

  def inner():
    print('Start')
    func()
    print('Finish')
  return inner

# Рекурсивная функиция это та которая в своем теле использует вызов самой себя