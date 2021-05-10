"""
Логиррование - запись данных о работе программы куда-то
Обычно логи записываются в отдельные файлы
Для Логирования используется встроенный модуль logging


Конфигурация логирования в Python состоит из четырех частей:

Loggers(Логеры)
Handlers(Обработчики)
Filters(Фильтры)
Formatters(Форматер)

Python определяет следующие уровни логирования:

DEBUG: Низкий уровень логирования системной информации для последующего использования в отладке

INFO: Общая системная информация

WARNING: Информация о мелких проблемах возникших при работе приложения

ERROR: Информация об ошибках возникших при работе приложения

CRITICAL: Информация о критических ошибках

Каждое сообщение записанное в логер называется Log Record(Запись).
"""

