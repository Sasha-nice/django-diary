from django.db import models


# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=64, verbose_name='Упражнение')
    musc = models.CharField(max_length=64, verbose_name='Мышечная группа', default='-')

