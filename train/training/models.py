from django.db import models
from exercise.models import Exercise

# Create your models here.


class Training(models.Model):
    #type = models.CharField(max_length=32, verbose_name='Тип тренировки', null=True)
    date = models.CharField(max_length=32, verbose_name='Дата', null=True)
    exercise = models.CharField(max_length=32, verbose_name='Упражнение', null=True)
    weight = models.IntegerField(verbose_name='Вес отягощения', null=True)
    number = models.IntegerField(verbose_name='Количество повторений', null=True)
    user = models.CharField(max_length=32, verbose_name='Пользователь', null=True)

