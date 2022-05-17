"""
Докер это средство упаковки, доставки в запуска приложений
У контейнера единый интерфейс
Единыый механизм запуска

Базовые сущности:
Образ(Image) - по сути это моя сборка, всё что я упаковал. Готовое к запуску приложение но не запущенное
Контейнер - это работающее приложение созданное на базе образа
Для контейнера образ является read only систмой

Докер хаб - реестр образов
Реестр образов находится локально

Установить Докер
Ok Google - install docker desktop

Как создать образ:
1. Нужен Dockerfile
2. Комманда docker build -t image-name dockerfile/location(can be ".")

Как удалить образ:
docker rmi image_name

Настройка Dockerfile:
FROM

RUN

WORKDIR

COPY

RUN

RUN

EXPOSE

ENV VAR VALUE

CMD

Контейнеры полностью изолированны!!! Если запустить контейнер который запустит локалхост на каком-то порте то у нас на
этом порте ничего не будет. Для того чтобы у нас тоже открылся такой порт на локалхосте нужно передать в запуске
контейнера дополнительный флаг -p conteiner_port:outside_port

Посмотреть контейнеры:
docker ps # Работающие контейнеры
docker ps -a # Все контейнеры

Запустить контейнер:
docker run image-name
or
docker run --name container_name image_name # in this terminal
docker run --name container_name -d image_name # daemon
docker run --name container_name -d --rm image_name # daemon + autodeleting after work finish
docker run --name container_name -d --rm -p 8000:8000 image_name # -||- + outside port
docker run --name container_name -d --rm -p 8000:8000 -e VAR=VALUE image_name # -||- + outside port + environment var
docker run --name container_name -d --rm -p 8000:8000 -e VAR=VALUE /
    -v /absolute/path/in_my_machine:/absolute/path/inside_container image_name # -||- + dynamic folder

Docker volume -ls # показывает какие у нас есть volumes. Устновка volume равносильна флагу -v
Docker volume create volume_name # создаётся volume

Остановить контейнер:
docker stop container_name

Удалить контейнер:
docker rm container_id/name # delete one container
docker rm $(docker ps -qa) # delete all containers

Настройка файла docker-compose.yaml
Для чего нужен docker-compose.yaml? Для того чтобы сделать над настройку над докером. Чтобы не прописывать например
тонну переменных окружения в команду run, можно такие вещи указать в файле docker-compose

"""