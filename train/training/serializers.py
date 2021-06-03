from training.models import Training
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class TrainingSerializer(serializers.ModelSerializer):
    def validate_number(self, value):
        if value < 0:
            raise ValidationError('Количество повторений должно быть неотрицательным')
        return value

    def validate_weight(self, value):
        if value < 0:
            raise ValidationError('Вес отягощения должен быть неотрицательным')
        return value


    class Meta:
        model = Training
        fields = ['id', 'date', 'exercise', 'weight', 'number', ]
