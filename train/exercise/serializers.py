from exercise.models import Exercise
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['name', 'musc', ]
