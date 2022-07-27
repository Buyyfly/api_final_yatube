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

1. Получить токен
POST запрос http://127.0.0.1:8000/api/v1/token/

