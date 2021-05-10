"""

Git — система управления версиями с распределенной архитектурой.
В отличие от некогда популярных систем вроде CVS и Subversion (SVN),
где полная история версий проекта доступна лишь в одном месте,
в Git каждая рабочая копия кода сама по себе является репозиторием

Это как сохранится в этапе прохождения компьютерной игры.

Гит позволяет учитывать не только историю кода который я сделал сам но и для любого количeевства програмистов

Системы контроля версий бывают распределенный и централизованные:

GIT является рспределенной сисемой контроля версий

Централизованная система это когда есть один сервер, один репозиторий который хранит всю историю проекта. И
програмисты подключаясь к репозиториию получают код, с ним работают и передают свои изминения на сервер

Распределенная система: у каждого разработчика есть своя копия историй проекта и они могут в произвольном порядке
обмениваться с друг другом изминениями которые они вносят в проект

Репозиторий - Хранилище с кодом

Камит - фиксация изминений или конкретная версия репозитария

бренч(ветка) - Альтернативная реальность кода история которого начинается от конкретного камита

Как все обычно происходит и какие основные команды:
1. Есть мастер копия. Главный репозиторий. Ориджин
2. Из репозитория делаются копии на рабочие компы разработчиков с помощью команды Git clone
3. Каждый разработчик фиксирует свои изминения с помощью команды Git commit
4. Изминения передаются на Ориджин через команду git push
5. Чтобы получить изминения которые сделали другие програмисты на своем компьютере используется команда git pull.
Тогда эти изминения попадут в локальный репозиторий отдельного программиста

Ветка это альтернативное изминение к какому-то камиту

Основные ветки называются Мастер. А альтернативная как-то по другому. Чтобы влить изминения из альтернативной ветки

в ветку мастер нужно использовать команду git merge

1. Поэтому первый шаг который нужно сделать это получить рабочую копию основного репозитория
2. Если я хочу добавить ещё какие-то файлы то есть команда git add
3. Зафиксировать эти изминения с командой git commit
4. Если надо загрузить эти файлы на сервер то используем git push

Файл .gitignore хранит в себе те директории отсеживать и контролировать которые не нужно. Это venv, .idea

Лучше сделать 10 маленьких камитов чем один большой.

Итак! Работа с GIT в PyCharm............................................................................................

1. Enabled VSC в вкладке VCS
	Создать локальный репозиторий в папке проекта через команду git init
2. Create .gitignore file and ADD there /venv/ and /.idea/ directory

3. Create git user name and email
	-Open the command line.
	-Set your username: git config --global user.name "FIRST_NAME LAST_NAME"
	-Set your email address: git config --global user.email "MY_NAME@example.com"

4. ADD to VCS required files(нужные файлы)
	Чтобы добавить в отслеживаемые файлы необходимые файлы, можно выбрать их + ПКМ + ADD to VCS или воспользоваться
	командной строкой. Сначало вызвать команду git status в которой будет видно какой файл в каком состоянии
	находится и там же будет подсказка какую команду использовать чтобы поменять статус файла. Написать git add filename
#Перед тем как сделать камит, нужно Обязательно ПРОВЕРИТЬ РАБОТОСПОСОБНОСТЬ СКРИПТА, пересмотреть все файлы которые мы
#меняли и только потом камитить.
5. Commit required files and point out(Указать) required comment
	Чтобы добавить необходимые файлы в commit, можно выбрать их + ПКМ + Commit file или воспользоваться
	командной строкой. Сначало вызвать команду git status в которой будет видно какой файл в каком состоянии
	находится и там же будет подсказка какую команду использовать чтобы поменять статус файла. Написать git commit -m
	"some comment"
6. В случаее работы с отдельной веткой за основу которой взята мастер ветка. Необходимо:
	а) Создать отдельную ветку через консоль ==> git checkout -b name_new_branch или в панели git + log + ПКМ на
	ветку мастера New branch from selected
	#Для того чтобы посмотреть какие вообще есть ветки в репозитории делается команда git branch -a
	б) В случаее необходимости слияния отдельной ветки с мастер веткой сначало необходимо перейти на ветку мастера
	через консольную команду git checkout master или в панели git + log + ПКМ на ветку мастера + Checkout. Далее
	делается консольная команда git merge name_of_branch. Или в панели git + log + ПКМ на ветку мастера + Checkout
	потом ПКМ на ветку которую хотим смёржить и Merge into Current(Слияние с текущей веткой)
	в) После слияния какогото бранча в мастер его можно удалить с помощью команды git branch -d name_of_branch. Или с
	панели git + log + ПКМ на ветку которую нужно удалить + delete
	г) Чтобы перейти в ветку мастера используется команда консоли git checkout master или на панели git выбрать ПКМ
	ветку мастера + Checkout

Как взаемодействовать с другими разработчиками.

1. Должен быть главный сервер типо GitHub

2. Дальше нужно создать репозиторий на сервере

3. Сделать pull имеющегося репозитория чтобы работаться с веткой мастер у себя локально или залить свои локальные
файлы на новосозданный репозиторий

4. Чтобы залить свои файлы на новосозданный репозиторий нужно скопировать гит ссылку в формате либо SSH или HTTPS
разница в том что при работе с HTTPS будет запрашеваться логин и пароль, а при использовании SSH это запрашеваться не
будет но нужно будет сделать отдельные определенные настройки. Скопированную ссылку находясь на ветке масте вставлем в
команду
git remote add test2 URL
где test2 – названия Вашего репозитория,

URL – URL-адрес Вашего репозитория.
Чтобы посмотреть все подключенные репозитории воспользуйтесь командой:

git remote -v

git rm -r --cached filename or foldername - удаляет файлы из индекса сохраняя их в локальном репозитории

git add . -
"""
