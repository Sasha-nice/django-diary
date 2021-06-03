from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from training.forms import TrainingForm
from django.http import JsonResponse
from training.models import Training
from django.conf import settings
from users.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from application.tasks import send
import elasticsearch
from training.serializers import TrainingSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.urls import resolve, reverse
from application.settings import LOGIN_URL


class TrainingViewSet(viewsets.ModelViewSet):
    serializer_class = TrainingSerializer
    queryset = Training.objects.all()
 #TODO метод к /1/

    def list(self, *args, **kwargs):
        print('list', args, kwargs)
        return super().list(*args, **kwargs)


def login_required(function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect('/login/', next = request.path)
        else:
            return function(request, *args, **kwargs)
    return wrapper


def log_on_email(func):
    def wrapper(self, *args, **kwargs):
        tr = Training.objects.all()
        cur = len(tr)
        func(self, *args, **kwargs)
        tr = Training.objects.all()
        cur1 = len(tr)
        if cur1 > cur:
            send.delay()
        return func(self, *args, **kwargs)
    return wrapper


def post_from_get(request):
    tr = Training()
    tr.date = '15.05'
    tr.number = 12
    tr.user = request.user.id
    tr.exercise = 'pup'
    tr.weight = 19
    tr.save()
    return JsonResponse({'status':'created'})


@login_required
@csrf_exempt
def get_post(request):
    if request.method == 'GET':
        tr = Training.objects.filter(user=request.user.id)
        data = [{'date': i.date, 'exercise': i.exercise, 'number': i.number, 'id': i.id} for i in tr]
        return JsonResponse({'exercises': data})
    elif request.method == 'POST':
        param = request.GET.dict()
        tr = Training()
        tr.date = param['date']
        tr.exercise = param['exercise']
        tr.weight = param['weigth']
        tr.number = param['number']
        tr.user = request.user
        tr.save()
        return JsonResponse({'status': 'created'})
    else:
        return JsonResponse({'status': 'bad_request'}, status=405)


@login_required
@csrf_exempt
def get_put_delete(request, iid):
    if request.method == 'DELETE':
        tr = Training.objects.filter(user=request.user)
        for i in tr:
            if i.id == iid:
                i.delete()
        return JsonResponse({'status': 'deleted'})
    elif request.method == 'PUT':
        tr = Training.objects.filter(user=request.user)
        for train in tr:
            if train.id == iid:
                params = request.GET.dict().keys()
                for i in params:
                    #setattr(train, i, request.GET.dict()[train])
                    #train.date = request.GET.dict().get('date', train.date)
                    #train.date = request.GET.dict()['date']
                    exec('train.' + i + ' = request.GET.dict()["' + i + '"]')
                train.save()
        return JsonResponse({'status': 'updated'})
    elif request.method == 'GET':
        try:
            data = {'status': 'Not found'}
            tr = Training.objects.filter(user=request.user)
            for i in tr:
                if i.id == iid:
                    data = {'date': i.date, 'exercise': i.exercise, 'number': i.number}
            return JsonResponse(data)
        except ValueError:
            JsonResponse({'status': 'not found'}, status=404)
    else:
        return JsonResponse({'status': 'bad_request'}, status=405)


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def centrifugo(request):
    return render(request, 'index.html')


def cen(request):
    data = {"1": "2"}
    return JsonResponse(data)


def elastic():
    es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])
    index_name = "training"
    tr = Training.objects.all()
    id = 200
    for i in tr:
        doc = {
            "date": i.date,
            "exercise": i.exercise,
            'weight': i.weight,
            'number': i.number,
            'id': i.id,
        }
        es.index(index=index_name, id=id, body=doc)
        id += 1


@csrf_exempt
@log_on_email
def post_form(request):
    form = TrainingForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'created'})
    return JsonResponse({'status': 'error'})
#render TODO


def search(request, field):
    es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])
    index_name = "training"
    doc = \
    {
     'query': {
         'match_all': {}
     },
     'fields': [field],
     '_source': 'false',
    }
    res = es.search(index=index_name, body=doc)
    data = set()
    for i in res['hits']['hits']:
        print(i['fields'][field][0])
        data.add(i['fields'][field][0])
    data = list(data)
    return JsonResponse({field: data})


def search1(request, field, value):
    es = elasticsearch.Elasticsearch()
    if es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    index_name = "training"
    doc1 = {
        "query": {
            "dis_max": {
                "queries": [
                    {
                        "match": {
                            field: value
                        }
                    },
                ]
            }
        }
    }
    res = es.search(index=index_name, body=doc1)
    data = {}
    count = 1
    for i in res['hits']['hits']:
        data['id'] = i['_id']
        data[count] = i['_source']
        count += 1
    return JsonResponse(data)
