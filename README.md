# Yatube API — REST API социальной сети блогов

API для соцсети Yatube: публикации, комментарии, сообщества и подписки на авторов.

## Возможности

- Публикации с пагинацией (limit/offset); изменять и удалять запись может только её автор.
- Комментарии к публикациям.
- Сообщества (группы) — только для чтения.
- Подписки на авторов и поиск по своим подпискам.
- Аутентификация по JWT: создание и обновление токена.

## Технологии

Python 3.10+, Django 5.2, Django REST Framework, Simple JWT, Djoser, django-filter, SQLite, pytest.

## Как запустить

```bash
git clone https://github.com/Vantied/api-final-yatube.git
cd api-final-yatube
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd yatube_api
python manage.py migrate
python manage.py runserver
```

API доступен по адресу `http://127.0.0.1:8000/api/v1/`.

## Пример запросов

```http
POST /api/v1/jwt/create/
{"username": "user", "password": "password"}

GET /api/v1/posts/?limit=10&offset=0
Authorization: Bearer <token>

POST /api/v1/follow/
{"following": "author_username"}
```

## Автор

Иван Богатов — [GitHub](https://github.com/Vantied) · Telegram [@Ivan_bogatov55](https://t.me/Ivan_bogatov55)
