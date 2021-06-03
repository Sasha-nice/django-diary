from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import JsonResponse
from django.template import Template
from django.template.loader import get_template


@csrf_exempt
def show_all(request):
    if request.method == 'GET':
        return JsonResponse({'status': 'good'})
    else:
        return JsonResponse({'status': 'bad'}, status=405)
