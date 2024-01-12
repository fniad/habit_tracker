# habit_tracker -- DRF-project: трекер привычек

## Функционал

По книге Джеймса Клира "Атомные привычки". В книге хороший пример привычки описывается как конкретное действие, которое можно уложить в одно предложение: "я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]". За каждую полезную привычку необходимо себя вознаграждать или сразу после делать приятную привычку. Но при этом привычка не должна расходовать на выполнение больше 2 минут.
Всё это принято за отправную точку, и данная концепция легла в основу приложения


## Инструкция по запуску проекта на ОС Linux Ubuntu

### Шаг 1. Клонирование репозитория

1. ```git clone https://github.com/fniad/habit_tracker.git```
2. ```cd habit_tracker```

### Шаг 2. Установка зависимостей

1. ```python3 poetry install```
2. ```poetry shell```

### Шаг 3. Установка и настройка Redis

1. ```sudo apt-get install redis-server```
2. ```sudo service redis-server start```
3. ```redis-cli ping``` (в ответ должно прийти **'PONG'**)

### Шаг 4. Установка и настройка PostgreSQL

1. ```sudo apt-get install postgresql```
2. ```sudo -u postgres psql```
3. ```CREATE DATABASE habit_tracker_db;```
4. ```\q```

### Шаг 5. Настройка окружения

1. ```touch .env```
2. ```nano .env``` и заполнить по шаблону из **.env.test**

### Шаг 6. Применение миграций

1. ```python3 manage.py migrate```

### Шаг 7. Загрузка данных с помощью команд 

1. ```python3 manage.py fill_db```

### Шаг 8. Создание суперпользователя

```python3 manage.py createsuperuser```

### Шаг 9. Запуск сервера
1. ```python3 manage.py runserver```

Для запуска DOCKER:

1.  На Ubuntu или Linux сначала остановить postgresql ```systemctl stop postgresql```
2. ```docker-compose build```
3. ```docker-compose exec app python manage.py migrate``` в соседнем терминале
4. ```docker-compose up```