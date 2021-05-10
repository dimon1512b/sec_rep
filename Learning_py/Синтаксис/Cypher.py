def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
def shift(power, side, letters, shift_letters):
    if side == 'right':
        for i in range(len(letters)):
            shift_letters.append(i - len(letters) + power % len(letters))
    elif side == 'left':
        for i in range(len(letters)):
            shift_letters.append(i - power % len(letters))
def myin_cypher():
    print('''Enter your cypher
:''')
    #Ввод примера шифрования и приобразование ввода в список с отдельными символами
    in_put = list(input())

    out_put = list(input())
    # Сопоставление символов в словарь
    cypher = {key:value for key, value in zip(in_put,out_put)}
    while True:
        choice = input('''What do you want???
encrypt or decrypt???
:''')
    #Ввод текста который нужно зашифровать и разбиение его по символам в список

        if choice == 'encrypt':

            encrypt = list(input('''What is your text?
:'''))
            # Ищем в словаре соответстрия нашего символа для шифровки с ключом словаря, а значением найденого ключа
            # будет символ которым нужно заменить наш
            for i in range(len(encrypt)):
                if encrypt[i] in cypher:
                    encrypt[i] = cypher[encrypt[i]]
            #Склееваем получившийся измененный список назад в строку
            print('Your result:')
            print(''.join(encrypt))
            break
        elif choice == 'decrypt':
            # Ввод текста который нужно розшифровать
            decrypt = list(input('''What is you text?
:'''))
            # Сопоставляем наш зашифрованый текст со значениями словаря и заменяем на ключ словаря для получения
            # розшифрованого символа
            for i in range(len(decrypt)):
                if decrypt[i] in out_put:
                    decrypt[i] = get_key(cypher, decrypt[i])
            # Склееваем получившийся измененный список назад в строку
            print('Your result:')
            print(''.join(decrypt))
            break
        else:
            print('Error enter, try again')
def сaesar_cypher():
    # Алфавиты
    eng_alphabet = list('abcdefghijklmnopqrstuvwxyz')
    rus_alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    ua_alphabet = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
    # Количесвтво букв в алфавите
    quantity_eng_letters = [i for i in range(26)]
    quantity_rus_ua_letters = [i for i in range(33)]
    # Списки с сдвинутыми значениями количества букв в алфавите
    shift_eng_letters = []
    shift_rus_ua_letters = []

    while True:
        # Пользователь выбирает язык и от этого все отталкивается
        language = input('''Choice language please: english or russian or ukrainian
:''')
        # Выбор стороны сдвига
        side_shift = input('''Choice side shift please: left or right
:''')
        # Сила сдвига
        power_shift = int(input('''Choice power shift
:'''))
        # Определение переменных в случае выбора того или иного языка
        if (language == 'english') and ((side_shift == 'left') or (side_shift == 'right')) \
                and (isinstance(power_shift, int) is True):
            language = eng_alphabet # Правильный алфавит
            letters = quantity_eng_letters # Правильное количество букв в алфавите
            shift_letters = shift_eng_letters # Сдвинутые значения количества букв в алфавите
            shift(power_shift, side_shift, letters, shift_letters) # Вызов функции здвига чтобы заполнить список
            #со здвинутыми значениями букв в алфавите
            # Создание словаря Ключ - буква, значение - здвинутый номер по порядку этой буквы
            shift_dict = {key: value for key, value in zip(eng_alphabet, shift_eng_letters)}
            break
        elif (language == 'russian') and ((side_shift == 'left' or side_shift == 'right')) \
                and (isinstance(power_shift, int) is True):
            language = rus_alphabet
            letters = quantity_rus_ua_letters
            shift_letters = shift_rus_ua_letters
            shift(power_shift, side_shift, letters, shift_letters)
            shift_dict = {key: value for key, value in zip(rus_alphabet, shift_rus_ua_letters)}
            break
        elif (language == 'ukrainian') and ((side_shift == 'left' or side_shift == 'right')) \
                and (isinstance(power_shift, int) is True):
            language = ua_alphabet
            letters = quantity_rus_ua_letters
            shift_letters = shift_rus_ua_letters
            shift(power_shift, side_shift, letters, shift_letters)
            shift_dict = {key: value for key, value in zip(ua_alphabet, shift_rus_ua_letters)}
            break
        else:
            print('''Error entering, try again''')
            #####
            #####
    # Создание сдвинутого алфавита
    shift_albhabet = [language[i] for i in shift_dict.values()]
    # Создание словаря Ключ - буква правильного алфавита, значение - соотведственная буква здвинутого алфавита
    shift_albhabet_dict = {key:value for key, value in zip(language, shift_albhabet)}
    en_decr = input("""What do you want: encrypt or decrypt?
:""") # Запрос на Шифровку или розшифровку на основании здвинутого словаря
    if en_decr == 'encrypt':
        encrypt = list(input("""Enter text for encrypt
:""")) # Запрос текста на шифровку сразу в тип списка
        # Проходимся по элементам текста иская их в ключах зашифрованого словаря
        for i in range(len(encrypt)):  # ['a', 'b', 'c', 'd']
            if encrypt[i] in shift_albhabet_dict:
                # Когда определяем что значение есть среди ключей словаря, меняем значение на значение со словаря
                encrypt[i] = shift_albhabet_dict[encrypt[i]]
        # Выводим результат склеевая его назад в строку
        print('Your encrypt text:')
        print(''.join(encrypt))
    elif en_decr == 'decrypt':
        decrypt = list(input("""Enter text for decrypt
:"""))
        for i in range(len(decrypt)):
            if decrypt[i] in shift_dict:
                decrypt[i] = get_key(shift_albhabet_dict, decrypt[i])
        print('Your decrypt text:')
        print(''.join(decrypt))

сaesar_cypher()

















