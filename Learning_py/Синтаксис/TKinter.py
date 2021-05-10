#from tkinter import *
#root = Tk()
# GUI - Graphical user Interface
import random
from tkinter import *
def hex_code_colors():
    red = hex(random.randrange(220,250))
    green = hex(random.randrange(170,180))
    blue = hex(random.randrange(0,1))
    red = red[2:]
    green = green[2:]
    blue = blue[2:]
    if len(red)<2:
        red = "0" + red
    if len(green)<2:
        green = "0" + green
    if len(blue)<2:
        blue = "0" + blue
    z = red + green + blue
    return "#" + z.upper()


'''Создаем главное окно win & root'''
'''wim.mainloop() - это режим постоянной активности окна'''

win = Tk()
photo = PhotoImage(file='icon.png') # Загружаем иконку в класс
win.iconphoto(False, photo) # Через метод активируем загруженную иконку
'''win.title - функция задающая название окну'''
win.title('Программа № 1') # Срокой задаем название

'''win.geometry - функция задающая размеры окна'''
win.geometry('800x600+385+10') # Указывать размеры необходимо через ИКС, ++ указывает смещение враво и вниз от левого
# верхнего угла для появления окна
win.resizable(True, True) # Разрешение на ростягивание по ширине или высоте
win.minsize(100, 100) # Ограничения по розтяжке окна минимальное
win.maxsize(1000, 1000) # Ограничения по розтяжке окна максимальное
win.config(bg=hex_code_colors()) # Указываем цвет фона #значит RGB формат



def get_name():
    value = name.get()
    if value:
        btn3['state'] = DISABLED

def command_for_btn3():
    name.insert(0, 'Вставленные слова')

def delete_entry():
    name.delete(0, 'end')

def counter():
    global count
    count += 1
    btn_count['text'] = 'Счетчик:' + str(count)
    btn_count['activebackground'] = hex_code_colors()
    btn_count['bg'] = hex_code_colors()
    if count % 2 == 0:
        btn_new_label['state'] = DISABLED
        btn1['state'] = DISABLED
        btn2['state'] = DISABLED
    else:
        btn_new_label['state'] = NORMAL
        btn1['state'] = NORMAL
        btn2['state'] = NORMAL
def color():
    win.config(bg = hex_code_colors())
    label_1['bg'] = hex_code_colors()
    label_2['bg'] = hex_code_colors()
def command_for_btn1():
    print('Hello, button_1 works!')
def command_for_btn2():
    print('Hello, button_2 works!')

def command_for_new_label():
    global count2
    count2 += 1
    label = Label(win, text='Text of label', bg = hex_code_colors())
    label.grid()
count = 0
count2 = 0

def press_key(event): # Функция события по умолчанию должна принимать один аргумент
    print(event) #char = {str} 'a'
#                 #delta = {int} 0
#                 #height = {str} '??'
#                 #keycode = {int} 65
#                 #keysym = {str} 'a'
#                 #keysym_num = {int} 97
#                 #num = {str} '??'
#                 #serial = {int} 226
#                 #state = {int} 0
#                 #time = {int} 43454734
#                 #type = {EventType} 2
#                 #num = {str} '??'
#                 #Winget = {TK} .
#                 #width = {str} '??'
#                 #x = {int} 279
#                 #x_root = {int} 879
#                 #y = {int} = 301
#                 #y_root = {int} 382
    if event.char == '\x08':
        name.delete(0, 'end')
    elif event.char == '\r':
        Label(win, text=name.get(), bg = hex_code_colors()).grid()
        name.delete(0, 'end')
    else:
        name.insert(INSERT, event.char)
#######################################################################################################################
'''ВИДЖЕТЫ''' '''LABEL НЕОБХОДИМ ДЛЯ ОТОБРАЖЕНИЯ ТЕКСТОВОЙ ИНФОРМАЦИИ'''
#######################################################################################################################
# Создание лэйбла
label_1 = Label(win, text=' HELLO!!! ', # Выбираем окно и текст
                bg=hex_code_colors(), # Цвет фона
                fg='white', # Цвет шрифта
                font=('Arial', 12, 'bold'), # Вид шрифта
                padx=0, # Разширяем фон лэйбла по ИКСУ по отношению к тексту в пиксилях
                pady=0, # Разширяем фон Лэйбла по игрику по отношению к тексту в пиксилях
                width=0, # Указывает ширину самого фона лэйбла в символах
                height=0, # Указывает высоту самого лейбла в символах
                anchor='center', # Указывает расположение текста в рамках лейбла
                # North(n), South(s), West(w), East(e) or sw, se, nw, ne
                relief= RAISED, # Контур для фона лейбла
                bd = 5, # Указываем толщину контура для фона
                #justify=CENTER, # В случаее многострочной строки, прижимает весь текст в какуюто сторону
                cursor='heart' # Изминение курсора мыши при навидении на лейбл
                ) # Лэйбэл создан но его ещё нужно росположить на окне
label_2 = Label(win, text=' I\'m label_2 ', bg=hex_code_colors(), fg='white', font=('Arial', 12, 'bold'), padx=0, pady=0,
                width=0, height=0, anchor='center', relief= RAISED, bd = 5, #justify=CENTER,
                cursor='plus'
                )
label_3 = Label(win, text='Label_3', font=('Arial', 12, 'bold'), relief = RAISED, bd=5)
label_3.grid(row = 1, column = 5)
#label_1.pack(#anchor='e', # n, ne, e, se, s, sw, w, nw, or center
             #side='bottom'
             # -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
             ##)
#label_2.pack(#side='top', anchor='w'
    #)
label_1.grid(row = 0, column= 0, stick = 'snew')
label_2.grid(row = 1, column=0, stick='wesn')
#######################################################################################################################
'''ВИДЖЕТЫ''' '''BUTTON НЕОБХОДИМ ДЛЯ ОТОБРАЖЕНИЯ КНОПОК'''
#######################################################################################################################
btn1 = Button(win, text='Кнопка1',
              command= command_for_btn1,
              font = ('Arial', 12, 'bold')# Указываем функцию без скобок, тоесть без её вызова
              #anchor = 'e'
              )
btn2 = Button(win, text='Кнопка2', command=command_for_btn2, font = ('Arial', 12, 'bold')
              )
btn3 = Button(win, text='Кнопка3', command=command_for_btn3, font = ('Arial', 12, 'bold'))
btn_delete = Button(win, text='Delete', command=delete_entry, font = ('Arial', 12, 'bold'))
btn_new_label = Button(win, text='''Create 
new label''', command=command_for_new_label, font = ('Arial', 12, 'bold'), padx= 0,
                       pady = 0, justify = CENTER)
btn_count = Button(win, text='Счетчик:' + str(count),command = counter, bg = hex_code_colors(),
                   activebackground = hex_code_colors(),
                   anchor = CENTER, font = ('Arial', 12, 'bold'))
btn_new_color = Button(win, text = 'Change color', command = color, font = ('Arial', 12, 'bold')
                       )
btn_entry = Button(win, text='Имя:', bg = hex_code_colors(),font = ('Arial', 12, 'bold'),
      padx=20, command=get_name, state = NORMAL)
btn1.grid(row = 2, column= 0, stick = 'we')
btn2.grid(row=0, column= 1, stick='we')
btn3.grid(row=5, column= 0, stick='we')
btn_delete.grid(row=4, column= 0, stick='we')
btn_count.grid(row=3, column=0, columnspan=2, stick='we')
btn_entry.grid(row=0, column=5, stick = 'wesn')
btn_new_color.grid(row = 2, column= 1, stick = 'wesn')
btn_new_label.grid(row=1, column=1, stick = 'we')
#    )
#btn2.pack(#side='left', anchor='s'
#    )
#btn_new_label.pack(#side = 'bottom'
#    )
#btn_count.pack(#side = TOP, anchor = CENTER
#    )
#btn_new_side.pack()
#btn_new_color.pack()

#FOR для создания кнопок в колонках

for i in range(3,5):
    for j in range(5):
         Button(win, text=f'Hello {i} {j}' ).grid(row=j, column=i, stick='wesn')
win.grid_columnconfigure(3, minsize=100) #Минимальная ширина колонки
win.grid_columnconfigure(4, minsize=100) #Минимальная ширина колонки

#######################################################################################################################
'''ВИДЖЕТЫ''' '''ENTRY НЕОБХОДИМ ДЛЯ ВВОДА ДАННЫХ'''
#######################################################################################################################

name = Entry(win, bg=hex_code_colors())
name.grid(row=0, column=6, stick = "sn")
#У Entry есть метод получения вводимых данных >> name.get() >> 'str'
#У Entry есть метод удаления вводимых данных >> name.delete(int(start), int(finish) or str('end')) >> ...
#Первый аргумент методы обязательный это от какого индекса начинать очистку
#Если указать только первый аргумент то удаляться будет только указанный индекс
#У Entry есть метод вставки необходимых данных >> name.insert(int(index), str('text') >> 'str'
#Вставка произойдет на место указанного индекса со здвигом всего остального в право

#Пример вставки - Кнопка 3



#######################################################################################################################
'''ОБРАБОТЧИК СОБЫТИЙ''' '''BIND НУЖЕН ДЛЯ РЕАКЦИИ НА СОБИТИЯ В ОКНЕ'''
#######################################################################################################################
# Первый аргумент указывает какой тип событий мы обрабатываем. Он указывается в кавычках '<>'
# Вторым аргументом указывается функция которая будет выполняться при наступлении указанного события
win.bind('<Key>', press_key) # Key - это событие обрабатывает любое нажатие на клавишу





'''quit() Остонавливает mainloop'''
#button = Button(root, text="Закрыть программу", command = root.quit
win.mainloop()