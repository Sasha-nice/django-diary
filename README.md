# django-diary

Учебное приложение на джанго  
API "Дневник тренировок"  
База данных db.sqlite3  
Структура проекта отличается от дефолтной:  
Приложение с settings.py называется application  
Модели подключены в админку  
Есть работа с django-rest-framework  
Созданы маршруты для DRF  
Написано несколько форм и валидация к ним  
Реализована OAuth2-авторизация через facebook  
Реализована отправка сообщений админу и периодические таски через celery  
В API использована работа с Elasticsearch для поиска по тренировкам  
Написан Dockerfile для сборки проекта через requirements.txt  
Переменные SECRET_KEY SOCIAL_AUTH_FACEBOOK_KEY SOCIAL_AUTH_FACEBOOK_SECRET EMAIL_PORT  
EMAIL_HOST_USER EMAIL_HOST_PASSWORD находятся в local_settings и отсутсвуют в репозитории
