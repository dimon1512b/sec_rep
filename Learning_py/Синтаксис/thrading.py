import threading
import time


def thread_function(name, delay):
    print(f"Thread {name} started")
    for i in range(5):
        print(f"Thread {name}: {i}")
        time.sleep(delay)
    print(f"Thread {name} finished")

# Створюємо два потоки
thread1 = threading.Thread(target=thread_function, args=("First", 1))
# Потік з іменем First, з затримкою 1 секунда ^

thread2 = threading.Thread(target=thread_function, args=("Second", 2))
# Потік з іменем Second, з затримкою 2 секунди ^

# Запускаємо потоки
thread1.start()
thread2.start()

# Очікуємо завершення обох потоків
thread1.join()
thread2.join()

print("Both threads have finished execution")
