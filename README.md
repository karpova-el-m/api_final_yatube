## Описание проекта:

Первая версия API для проекта Yatube.

Позволяет:

* Реализовывать методы GET, POST, PATCH, PUT, DELETE для моделей Post и Comments;
* Реализовывать методы GET и POST для модели Follow;
* Реализовывать метод GET для модели Group;
* Авторизовываться и аутентифицироваться через JWT-токен;
* Разграничивать доступ для неавторизованных, авторизованных пользователей и авторов;

## Установка:

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/karpova-el-m/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры некоторых запросов к API:

### Для неавторизованных пользователей (доступ только в режиме чтения).

Получение всех постов:

```
GET http://127.0.0.1:8000/api/v1/posts/
```
При указании параметров offset и limit выдача работает с пагинацией:

```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
```

Получение всех комментариев:

```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

```

```
[
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
]
```

Получение отдельного комментария:

```
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

```

```
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```

### Для авторизованных пользователей.

Создание комментария:

```
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Редактирование комментария:

```
PUT http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

```

Частичное редактирование комментария:

```
PATCH http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

```

Удаление комментария:

```
DELETE http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```
