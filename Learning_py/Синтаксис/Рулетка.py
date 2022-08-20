from random import randint

counter_black = 0

counter_white = 0

counter_zero = 0

counter_same_colour = {
    'colour': '',
    'max_same': 1,
}

previous_clot = None

money = 100000

counter_max_money = money

pay = float(input('pay: '))

PAY = pay

black = {i for i in range(1, 37) if i % 2 == 0}

white = {i for i in range(1, 37) if i % 2 != 0}

zero = 0

rate = black

while 1200000 > money > 0:

    print(f'{money = }')

    if (money - pay) < 0:
        pay = money
        money -= pay
    else:
        money -= pay

    slot = randint(0, 37)

    if slot in black:
        print('slot is Black')
        counter_black += 1
        if previous_clot == 'black':
            counter_same_colour['max_same'] += 1
        else:
            counter_same_colour['max_same'] = 1
        previous_clot = 'black'
    elif slot in white:
        print('slot is White')
        counter_white += 1
        if previous_clot == 'white':
            counter_same_colour['max_same'] += 1
        else:
            counter_same_colour['max_same'] = 1
        previous_clot = 'white'
    else:
        print('slot is ZERO!!!')
        counter_zero += 1
        if previous_clot == 'zero':
            counter_same_colour['max_same'] += 1
        else:
            counter_same_colour['max_same'] = 1
        previous_clot = 'zero'
    counter_same_colour['colour'] = previous_clot
    if slot in rate:
        money += pay * 2
        if pay > PAY:
            if rate == white:
                rate = black
            else:
                rate = white
        if money > counter_max_money:
            counter_max_money = money
        pay = PAY
    else:
        if pay == PAY ** 4:
            continue
        else:
            pay *= 2
print('Start money = 100000')
print('Actual money = ' + str(money))
print('White counter = ' + str(counter_white))
print('Black counter = ' + str(counter_black))
print('Zero counter = ' + str(counter_zero))
print('Max same = ' + str(counter_same_colour))
print('Max money = ' + str(counter_max_money))
