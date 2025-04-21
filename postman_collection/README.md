# API для Yatube

## Описание
API для социальной сети блогеров Yatube. Предоставляет возможности для публикации постов, комментирования, подписки на авторов и работы с группами контента.

## Функциональность
- Просмотр, создание, обновление и удаление публикаций
- Просмотр и создание групп
- Комментирование публикаций
- Управление подписками на авторов
- Аутентификация по JWT-токену

## Технологии
- Python 3.7+
- Django 3.2
- Django REST Framework
- REST API
- JWT-аутентификация

## Установка

Клонировать репозиторий:
```
git clone https://github.com/username/api_final_yatube.git
```

Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

Установить зависимости:
```
pip install -r requirements.txt
```

Выполнить миграции:
```
python manage.py migrate
```

Запустить проект:
```
python manage.py runserver
```

## Примеры запросов API

### Получение токена
```
POST /api/v1/token/
{
    "username": "username",
    "password": "password"
}
```

### Получение списка публикаций
```
GET /api/v1/posts/
```

### Создание публикации
```
POST /api/v1/posts/
{
    "text": "Текст публикации",
    "group": 1
}
```

### Получение комментариев к публикации
```
GET /api/v1/posts/{id}/comments/
```

### Подписка на автора
```
POST /api/v1/follow/
{
    "following": "username"
}
```

## Документация API
После запуска проекта полная документация доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

## Автор
Ваше имя