# Напишіть функцію на Python, яка приймає як аргумент рядок з ім'ям файлу і
# повертає розширення файлу (частина рядка після останньої точки):
#
# не використовуючи побітовий зсув;
# враховувати, що точок може бути у рядку кілька;
# ігнорувати випадки, коли точка знаходиться на початку або наприкінці імені файлу;
# якщо розширення не знайдено – зробити виняток (exception).


def get_file_extension(filename: str) -> str:
    filename = filename.strip(".")
    last_dot_index = filename.rfind(".")

    if last_dot_index == -1:
        raise ValueError("File without extension")

    return filename[last_dot_index + 1:]


# приклад використання:
if __name__ == "__main__":
    try:
        ext = get_file_extension("...example.a...asd...ss..")
        print(f"Расширение файла: '{ext}'")
    except ValueError as e:
        print(e)
