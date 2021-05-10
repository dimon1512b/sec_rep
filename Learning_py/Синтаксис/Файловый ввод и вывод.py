# Function "open" принимает аргумент в виде полного пути к файлу который нужно считать
inf = open('file.txt', 'r') #open('file.txt.')
s1 = inf.readline() # .readline принимает строчку для чтения из файла
s2 = inf.readline() # Аргументов не принимает. Следующий вызов читает следующую строчку
s3 = inf.read() # Читает весь файл сразу
s4 = inf.read(5) # Читает количество символов
s5 = inf.read(5) # Читает следующие 5 символов
inf.seek(0) # Указывает на символ с которого нужно начать следующий .read
inf.close() # Закривает файл

# r Значит что мы собираемся читать данный файл

# Другой способ подключиться к файлу чтобы не закривать его в ручную
with open('dictionary.py', 'r') as inf:
    s1 = inf.readline()
    s2 = inf.readline()
# Здесь файл уже закрыт
# Переменной inf уже нет. Такой путь удобен и рекомендуется

# Чтобы не читать а записывать что-то в файл вместо r ставим w(write) и команду write

with open('dictionary.py', 'w') as ouf: # Открываем файл на запись и подвязываем его к переменной. Удаляет все данные с
    #
    ouf.write('SomeText\n') # В этом блоке выполняем работу с записью в файл
    ouf.write(str(25))
with open(r'C:\Users\user\PycharmProjects\pythonProject\dataset_3380_5.txt', 'w', encoding='utf-8') as txt:
    for i in dict_lst:
        txt.write(str(i))
        txt.write(' ')
        txt.write(str(dict_lst[i]))
        if get_key(dict_lst, dict_lst[i]) == 11:
            break
        else:
            txt.write('\n')
# Здесь файл уже закрыт

# Метод чтения файла - .strip()
'\t abc \n '.strip() ==> 'abc'

# Метод подстроиться под любую ОС и подключиться к файлу правильным синтаксисом:::

import os
os.path.join('..', 'dirname', 'filename.txt') == > './dirname/filename.txt'

with open('C:\\Users\\user\\PycharmProjects\\pythonProject\\dataset1.txt', encoding= 'utf - 8') as text:
    text = text.read()
    print(text)

# Как прочитать все строчки из файла:::

with open('file.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)



# У функции open много параметров, они указаны в статье "Встроенные функции", нам пока важны 3 аргумента:
# первый, это имя файла. Путь к файлу может быть относительным или абсолютным.
# Второй аргумент, это режим, в котором мы будем открывать файл.
#
# Режим	Обозначение
# 'r'	открытие на чтение (является значением по умолчанию).
# 'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a'	открытие на дозапись, информация добавляется в конец файла.
# 'b'	открытие в двоичном режиме.
# 't'	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись
# Режимы могут быть объединены, то есть, к примеру, 'rb' - чтение в двоичном режиме. По умолчанию режим равен 'rt'.
#
# И последний аргумент, encoding, нужен только в текстовом режиме чтения файла. Этот аргумент задает кодировку.
# Например encoding = 'utf - 8' позволяет читать кирилицу
