# Task manager

Тестовая задача по реализации небольшого проекта с регистрацией пользователей и добавлением задач.

Проект реализован на Django с использованием DRF для реализации RESTful API, в качестве базы данных используется PostgreSQL.

## Запуск проекта локально
Проект использует poetry для менеджмента зависимостей и virtualenv'ов, docker и docker-compose для контейнеризации.
Прежде всего нужно установить poetry - [ссылка на доку](https://poetry.eustace.io/docs/)

Далее:

1. Установка зависимостей проекта <br>`$ poetry install`
2. Активация virtualenv<br> `$ poetry shell`
3. Билд приложения<br> `$ docker compose build`
4. Запуск бд и приложения<br> `$ docker compose up -d`
5. Для запуска тестов<br> `$ pytest src/`

Приложение находится на порту 8000, так что можно обращаться к апи по адресу http://localhost:8000/api/

Swagger находится по пути `/api/swagger/`, redoc - `/api/redoc/`

Для автоматического запуска линтера и форматтера при коммитах
`$ pre-commit install`