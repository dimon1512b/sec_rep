#dictionary(Словарь, Асоциативный массив)

#Словарь - неупорядоченная коллекция произвольных обьектов с доступом по ключу

# Словари ИЗМЕНЯЕМЫ, НЕУПОРЯДОЧЕНЫ, ВСЕ КЛЮЧИ РАЗЛИЧНЫ, КЛЮЧИ НЕИЗМЕНЯЕМЫ

a = ['moskva', 'piter', 'penza']
#             Асоциации
#        0        1        2


#Первый способ создания словаря

d = {
    #key:value
    'moskva':495,
    'piter':812,
    'penza':8412
}
print(d)

#{'moskva': 495, 'piter': 812, 'penza': 8412}


# Второй способ создания словаря

#Функция dict (Создает словарь но работает только для стринг типа)

r = dict (moskva = 495, piter = 812, penza = 8412)
print(r)

#{'moskva': 495, 'piter': 812, 'penza': 8412}


#Третий способ создания словаря

a = [['moskva', 495], ['piter', 812], ['penza', 8412]]
t = dict(a)

print(t)

#{'moskva': 495, 'piter': 812, 'penza': 8412}

#Четвертый способ создания словаря(Метод .fromkeys())
#q = dict.fromkeys(['a', 'b', 'c'])
#print(q)
#{'a': None, 'b': None, 'c': None}
#Метод .fromkeys() автоматически превращает каждый элемент списка в ключ и присваевает ему значение либо None для всех
#Либо то что будет указано после списка. Метод может принимать только два аргумента

q = dict.fromkeys(['a', 'b', 'c'], 100)
print(q)

#{'a': 100, 'b': 100, 'c': 100}

#Обращение к элементам словаря по ключу

di = {
    'hello' : 'two'
}
print(di['hello'])
#two

#Можно указать к какому ключу в словаре мы обращаемся и задать ему значение после равно "="
di[4] = 'four'
print(di[4])
#four

# !!!

#ЧТОБЫ СОЗДАТЬ НОВУЮ ПАРУ НУЖНО К НЕСУЩЕСТВУЮЩЕМУ КЛЮЧУ ПРИСВОИТЬ НОВОЕ ЗНАЧЕНИЕ!!!

person = {}

s = 'Ivanov Ivan Samara SGU 5 4 5 5 4 3 5'
s = s.split()
person['last name'] = s[0]
person['first name'] = s[1]
person['city'] = s[2]
person['university'] = s[3]
person['marks'] = []
for i in s[4::]:
    person['marks'].append(i)
print(person)

#{'last name': 'Ivanov', 'first name': 'Ivan', 'city': 'Samara', 'university': 'SGU', 'marks': ['5', '4', '5', '5', '4', '3', '5']}

#Удаление пар в словаре

j = {
    'one': 1
}
del j['one']
print(j)

#{}

# Функции которые поддерживает словарь:
# len(выдает количество пар Ключ - Значение)
# in (True, False), in not
# for in: "For обходит КЛЮЧИ!!!"
for key in d:
    print(key, d[key])
#moskva 495
#piter 812
#penza 8412

#Методы словаря:

print(d.get('moskva')) # 495
print(d.get(1)) # None
print(d.get(2, "Not key")) #Not key
print(d.setdefault(1)) #None # В отличии от get этот метод создает в словаре ключ и значение None
print(d.setdefault(2, "two")) #two
print(d[2]) # two
print(d.pop('moskva')) # 495 # Принимает ключ, передает его значение и удаляет пару из словаря
print(d.get('moskva')) # None
print(d.popitem()) # (2, 'two') # Не принимает значений. Передает случайную пару и удаляет её из списка
print(d.keys()) # dict_keys(['piter', 'penza', 1]) # Передает множество ключей
print(d.values()) # dict_values([812, 8412, None]) # Передает множество значений
print(d.items()) # dict_items([('piter', 812), ('penza', 8412), (1, None)]) # Передает множество пар ключ - значение


#При заполнении словаря было очень удобно использовать функцию zip.
x = ['a','b','c']
y = ['e','f','g']
#будет сгенерирован список в виде [('a', 'e'), ('b', 'f'), ('c', 'g')]
d = {key:value for key,value in zip(x,y)}
#затем вывод, инверсия словаря и снова вывод.
#
#
