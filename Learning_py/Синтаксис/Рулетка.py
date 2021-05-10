from random import randint

counter_black = 0

counter_white = 0

counter_zero = 0

counter_max_money = 1000

money = 1000

pay = 2

PAY = pay

black = {

    i for i in range(1, 37) if i % 2 == 0

}

white = {

    i for i in range(1, 36) if i % 2 != 0

}

zero = 0

rate = black

while money < 1200 and money > 0:

    print(money)

    if (money - pay) < 0:
        pay = money
        money -= pay
    else:
        money -= pay

    slot = randint(0, 37)

    if slot in black:
        print('slot is Black')
        counter_black += 1
    elif slot in white:
        print('slot is White')
        counter_white += 1
    else:
        print('slot is ZERO!!!')
        counter_zero += 1

    if slot in rate:
        money += pay * 2
        if pay > 2:
            if rate == white:
                rate = black
            else:
                rate = white
        if money > counter_max_money:
            counter_max_money = money
        pay = 2

        continue
    else:
        if pay == PAY ** 4:
            continue
        else:
            pay *= 2
print('Start money = 1000')
print('Actual money = ' + str(money))
print('White counter = ' + str(counter_white))
print('Black counter = ' + str(counter_black))
print('Zero counter = ' + str(counter_zero))
print('Max money = ' + str(counter_max_money))