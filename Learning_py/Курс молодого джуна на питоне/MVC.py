"""

Model View Controller(MTV -Model template view) - шаблон предназначен для разделения различных частей программы на
разные абстрактные уровни
Представление отделить от модели(бизнесс Логики)

Модель взаемодействует с базой данных обменеваясь данными.
Модель задает поведение контроллеру
Контроллер взаемодействует в клиентом внося изминения в модели и базу данных и в Вью
Клинт взаемодействует с контроллером через Вью

Модель отвечает за доступ к данным

Вью отвечает за отображение данных

Контроллер отвечает за взаемодействие с пользователем

ORM — технология программирования, которая связывает базы данных с концепциями объектно-ориентированных языков
программирования, создавая «виртуальную объектную базу данных».

Model in django это структура данных которая будет храниться в базе данных

Выводить бизнес логику в отдельную директорию

"""