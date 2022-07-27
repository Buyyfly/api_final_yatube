# Описание

Проект «API для Yatube».

# Установка

1. Склонировать репозиторий
2. Создать вирутальное окружение
pythom -m venv venv
3. активировать вирутальное окружение
\venv\Scripts>activate.bat
4. Установить зависимости
pip install -r requirements.txt
5. Запустить сервер
python manage.py runserver

# Примеры

Для начала необходимо получить токен передав в формате json 
POST запрос http://127.0.0.1:8000/api/v1/jwt/create/
{
    "username": "user",
    "password": "pass"
}

1.Пример обращения к http://127.0.0.1:8000/api/v1/posts/
[
    {
        "id": 1,
        "author": "evgeniy",
        "text": "TestPost1",
        "pub_date": "2022-07-27T18:30:32.343475Z",
        "image": null,
        "group": 1
    }
]
2. Редиктирование поста http://127.0.0.1:8000/api/v1/posts/1/ 
{
    "id": 1,
    "author": "evgeniy",
    "text": "TestPost2",
    "pub_date": "2022-07-27T18:30:32.343475Z",
    "image": null,
    "group": 1
}
3. После удаления поста обратимся к нему и получим

{
    "detail": "Not found."
}


