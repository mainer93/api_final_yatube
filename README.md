Документация к API проекта Yatube

## Описание проекта
Создан проект API для Yatube, реализованы возможности создания, обновления, удаления публикаций; добавления, обновления, удаления комментариев; просмотра информации о сообществе; просмотр подписок. Также реализована аутентификация JWT

## Как запустить проект
1. Клонировать репозиторий и перейти в него в командной строке:
```git clone git@github.com:mainer93/api_final_yatube.git```
2. Cоздать и активировать виртуальное окружение:
```python -m venv env```
3. Обновить pip:
```python -m pip install --upgrade pip```
5. Установить зависимости из файла requirements.txt:
```pip install -r requirements.txt```
6. Запустить проект:
```python manage.py runserver```

# Некоторые примеры запросов к API
## 1) GET api/v1/groups
Вывод:
```
[
    {
        "id": 1,
        "title": "TestGroup",
        "slug": "test-group",
        "description": "Some text."
    }
]
```
## 2) POST /api/v1/posts/
Запрос:
```
{
    "text": "Пост с группой",
    "group": {{group_id}}
}
```
Вывод:
```
{
    "id": 4,
    "author": "regular_user",
    "text": "Пост с группой",
    "pub_date": "2024-04-20T16:07:08.209945Z",
    "image": null,
    "group": 1
}
```
