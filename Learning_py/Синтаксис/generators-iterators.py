"""
Генератор - итератор елементы которого можно обойти только один раз
Генератор сразу является итератором и поддерживает функцию next
Итератор - обьект который поддерживает функцию next
"""

s = [1, 2, 3]

s_iter = iter(s)

print(next(s_iter))  # 1
print(next(s_iter))  # 2
print(next(s_iter))  # 3

g = (i for i in range(5))

print(f'{g = }')

print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # 4


def gen_f():
    for i in range(5):
        yield i

"""
Наша функция генератор всегда запоминает какой елемент она отдала последний раз
при помощи оператора yirld и при следующем вызове она вернет следующий
"""

print(f'{next(gen_f()) = }')  # 0
for i in gen_f():
    print(i)

print(f'{sum(gen_f()) = }')

s = (i for i in range(4))

for i in s:
    print(i)

print(sum(s))  # 0
