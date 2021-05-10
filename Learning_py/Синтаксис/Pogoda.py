running = True
while running:
    pogoda = input("""Посмотрите в календарь и введите актуальную пору времени
сегодня, пожалуйста. Например \"Зима\":""")
    if pogoda == "Зима":
        print("Значит холодно!")
        running = False
    elif pogoda == "Лето":
        print("Значит жарко!")
        running = False
    elif pogoda == "Весна":
        print(" Значит нормально!")
        running = False
    elif pogoda == "Осень":
        print("Значит влажно!")
        running = False
    else:
        print("Чёт, братишка ты не так ввел походу... Попробуй ещё")
print("Конец")