from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    lastname = models.CharField(verbose_name='Фамилия', max_length=32, default='-')
    firstname = models.CharField(verbose_name='Имя', max_length=100, default='-')
    age = models.IntegerField(verbose_name='Возраст', default=0)
    weigth = models.IntegerField(verbose_name='Вес', default=0)

    def __str__(self):
        return self.lastname + "_" + self.firstname

    class Meta:
        ordering = ["firstname"]
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

