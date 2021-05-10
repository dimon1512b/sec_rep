#[выражение for i in коллекция]
a = [0 for i in range(7)] # [0, 0, 0, 0, 0, 0, 0]
print(a)
# Генерация списков!!!
# a = [0] * 5 ==> [0, 0, 0, 0, 0]
# a = [0 for i in range(5)] ==> [0, 0, 0, 0, 0] - Выражение 0 каждый раз заменяет переменную i
# a = [i for i in range(5)] ==> [0, 1, 2, 3, 4] - Переменная i вместо выражения возвращает каждое значение i
# a = [i**2 for i in range(5)] ==> [0, 0, 4, 9, 16] - Указали переменную в квадрате
# a = [i for i in "Hello"] ==> [H, e, l, l, o]

print(" ".join([ str(x) for x in b ]))




text = [int(i) for i in input().split()]
if len(text) == 1:
    print(text[0])
else:
    [print( text[i-1] + text[(i+1) % len(text)] ,end=' ') for i in range(len(text))]
    # выражение src[(i+1) % len(src)] на выходе для src = [1, 3, 5, 6, 10] даст [3, 5, 6, 10, 1]
    # потому, что (i+1) % len(src) даёт 1 2 3 4 0
    # т.е. таким образом 0й элемент оказывается в конце списка (как будто повернули циферблат)
    # таким образом если при обращении к i+1 случится выход за границу диапазона для последнего элемента
    # то при обращении к (i+1) % len(src) элементу выхода не произойдет
    # поэтому складывая -1й элемент с [(i+1) % len(src)]-тым элементом
    # мы выполним условие найти сумму предыдущего и следующего элементов
    # [print( src[(i+1) % len(src)]) for i in range(len(src))]
# Задача на вывод чисел в двойной матрице в виде улитки: С использованием listComprehension
arr = []
arr_2 = []
number = 0
n = int(input())
x = n
y = 0

for i in range(n):
  for j in range(n):
    arr_2.append(0)
  arr.append(arr_2)
  arr_2 = []

add = 1
while add <= n ** 2:
  while number != x:
    arr[y][number] = add
    add += 1
    number += 1
  if add == (n ** 2) + 1:
    break
  number = y + 1

  while number < x:
    arr[number][x - 1] = add
    number += 1
    add += 1
  if add == (n ** 2) + 1:
    break
  number = int(x - 2)

  while number >= y:
    arr[x - 1][number] = add
    number -= 1
    add += 1
  if add == (n ** 2) + 1:
    break
  number = x - 2

  while number != y:
    arr[number][y] = add
    add += 1
    number -= 1

  x -= 1
  y += 1
  number = y

for i in arr:
  print(*i)

# Для тех, кто хочет сократить свой код :) написал небольшое руководство по [list comprehension]
# на основе примера на stackoverflow.com
# # http://stackoverflow.com/questions/16632124/python-emulate-sum-using-list-comprehension
# я немного изменил этот пример, чтобы лучше объяснить работу [list comprehension]
# и вам было проще понять, как применить этот подход к решению задания

# допустим, у нас есть список фруктов, где зафиксированы самые низкие и высокие цены на эти фрукты
# т.е. по сути это список списков :)
lst = [["apple", 55, 62], ["orange", 60, 74], ["pineapple", 140, 180], ["lemon", 80, 84]]

# выведем этот список для нагляности на экран, используя [list comprehension]
[print(el) for el in lst]
# ['apple', 55, 62]
# ['orange', 60, 74]
# ['pineapple', 140, 180]
# ['lemon', 80, 84]

# если мы хотим подсчитать среднюю цену на каждый из фруктов, то напишем что-то вроде
sumMiddle = 0
for el in lst:
    sumMiddle = (el[1] + el[2]) / 2
    print(sumMiddle)

# или можно сделать это одной строкой
[print((priceLow + priceHigh) / 2) for fruit, priceLow, priceHigh in lst]
# представьте, что наш список списков - это таблица из трёх столбцов
# и мы можем обращаться к столбцам, просто озаглавив их fruit, priceLow, priceHigh
# в цикле for, почти как перебор элементов словаря for key, value in d.items() :)

# поэтому, когда вы захотите прикинуть, сколько же, от и до, в среднем может стоить
# ваша фруктовая корзина, нужно будет посчитать среднее по каждой колонке
# вы можете сделать это примерно так
sumLow, sumHigh = 0, 0
for el in lst:
    sumLow += el[1]
    sumHigh += el[2]
sumLow /= len(lst)
sumHigh /= len(lst)
print(sumLow, sumHigh)

# или применить кунг-фу списковых выражений и обойтись парой строк :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst))
print(sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# а где два принта, там и один :)
print(sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst), sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# надеюсь, вам было понятно и интересно
# желаю успехов в учёбе!!!


set_2 = {

    i for i in range(1, 37) if i % 2 == 0

}

set_3 = {

    i for i in range(1, 36) if i % 2 != 0

}

set_0 = [

    [i for i in range(3)] for j in range(5)

]

set_5 = {

    i * 2 for i in set_2

}

set_6 = [

    two for zero, one, two in set_0

]

sum_set_6 = [[sum([two for zero, one, two in set_0])] for i in range(sum([two for zero, one, two in set_0]))]

x = 0

for i in sum_set_6:
    i.append(x)
    x += 1

print(set_2)

print(len(set_2))

print(set_3)

print(len(set_3))

print(set_0)

print(set_5)

print(set_6)

print(sum_set_6)