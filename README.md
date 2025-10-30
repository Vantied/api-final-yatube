# Yatube API

## Описание

Проект **Yatube** — это социальная сеть для публикации постов, комментариев и подписки на авторов.
API предоставляет возможности:

- Создавать, читать, обновлять и удалять публикации.
- Просматривать и добавлять комментарии к публикациям.
- Просматривать списки сообществ.
- Подписываться на других пользователей и просматривать свои подписки.
- Получать JWT-токены для аутентификации.


## Установка

1. Клонировать репозиторий:

```bash
git clone https://github.com/Vantied/api-final-yatube.git
cd api-final-yatube
```

2. Создать и активировать виртуальное окружение:

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
source env\Scripts\activate     # Windows
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Выполнить миграции базы данных:

```bash
python manage.py migrate
```

5. Запустить сервер:

```bash
python manage.py runserver
```

API будет доступен по адресу: `http://127.0.0.1:8000/api/v1/`

## Примеры запросов к API

### Публикации (Posts)

- **Получить список публикаций с пагинацией**:

```http
GET /api/v1/posts/?limit=10&offset=0
```

- **Создать публикацию** (только авторизованный пользователь):

```http
POST /api/v1/posts/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "text": "Мой новый пост",
  "group": 1
}
```

### Комментарии (Comments)

- **Получить комментарии к публикации**:

```http
GET /api/v1/posts/1/comments/
```

- **Добавить комментарий к публикации**:

```http
POST /api/v1/posts/1/comments/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "text": "Отличный пост!"
}
```

### Сообщества (Groups)

- **Получить список сообществ**:

```http
GET /api/v1/groups/
```

- **Получить информацию о конкретном сообществе**:

```http
GET /api/v1/groups/1/
```

### Подписки (Follow)

- **Получить список подписок пользователя**:

```http
GET /api/v1/follow/?search=username
Authorization: Bearer <access_token>
```

- **Подписаться на пользователя**:

```http
POST /api/v1/follow/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "following": "other_user"
}
```

### Аутентификация (JWT)

- **Получить токен**:

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "user1",
  "password": "password123"
}
```

- **Обновить токен**:

```http
POST /api/v1/jwt/refresh/
Content-Type: application/json

{
  "refresh": "<refresh_token>"
}
```

- **Проверить токен**:

```http
POST /api/v1/jwt/verify/
Content-Type: application/json

{
  "token": "<access_token>"
}
```