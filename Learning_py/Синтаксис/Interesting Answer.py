first = float(input())
second = float(input())
action = input()
operations = {"mod": "%", "div": "//", "pow": "**"}
try:
    print(eval("(" + str(first) + ")" + operations.get(action, action) + str(second)))
except ZeroDivisionError:
    print('Деление на 0!')


if format[0] == "т":
a, b, c = int(input()), int(input()), int(input())
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a)
print(b)
print(c)


a, b, c = int(input()), int(input()), int(input())
max_int = max(a, b, c)
min_int = min(a, b, c)
print(max_int)
print(min_int)
print((a + b + c) - max_int - min_int)



i=int(input())
d=i%10
h=i%100
if d==1 and h!=11:
    s=""
elif 1<d<5 and not 11<h<15:
    s="а"
else:
    s="ов"
print(i," программист"+s)

a, b, c, d, e, f = input()
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


def modify_list(l):
    l[:] = [i//2 for i in l if i % 2 == 0]