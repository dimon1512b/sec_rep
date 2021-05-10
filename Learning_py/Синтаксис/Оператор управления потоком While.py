#Оператор while позволяет многократно выполнять блок команд
#до тех пор, пока выпол- няется некоторое условие.
# if может быть с двойным условием:
number1 = 1
number2 = 3
print("Угадай два числа от 1 до 3)))")
running = True
while running:
    guess1 = int(input("Угадай первое число:"))
    guess2 = int(input("Угадай второе число:"))
    if guess1 == number1 and guess2 == number2:
        print("Молодец ты угадала оба числа")
        running = False
    elif guess1 == number1 and guess2 != number2:
        print("Ты угадала первое число но не угадала второе")
    elif guess1 != number1 and guess2 == number2:
        print("Ты угдала второе число но не угадала первое")
    else:
        print("К сожалению ты не угадала ни одно число(((")
else:
    print("Finish")
i = 1
while i <= 5:
    print(i)
    i = i + 1
i = 1
#Break
while i >= 0:
    print(i)
    i = i + 1
    if i == 1000:
        print(i)
        break
#Countinue - игнорирует все что идет дальше после него повторяя цикл
number = 1
while number <= 1000:
    number += 1
    if (number % 2) != 0:
        continue;
    print("Четные числа:" + str(number))
number = 1
while number <=100:
    number += 1
    if (number % 2) == 0:
    #Строка вверху значит: Если остаток от деления Намбера на 2 будет равен 0(тоесть намбер поделился на 2 без остатка)
    # тогда выполнить следующий код. Поделится на два без остатка может только кратное двом число
        print("Четные числа:" + str(number))
