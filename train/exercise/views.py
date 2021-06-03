from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from exercise.models import Exercise

from exercise.serializers import ExerciseSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()
