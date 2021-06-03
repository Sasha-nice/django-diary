from celery import shared_task
from training.models import Training
from django.core.mail import send_mail


@shared_task
def add(a, b):
    return a + b


@shared_task
def add1(a, b):
    with open(f'data', "a") as f:
        f.write(str(len(Training.objects.all())) + '\n')
    return 1


@shared_task
def send():
    send_mail('New object', 'New object in db', 'server-email',
              ['admin email'])
    return 123
