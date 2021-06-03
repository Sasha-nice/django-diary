from users.models import User
from rest_framework import serializers
from rest_framework.serializers import ValidationError
import re


class UserSerializer(serializers.ModelSerializer):

    def validate_lastname(self, value):
        if re.match('^[А-ЯЁ][а-яё]+', value):
            return value
        return ValidationError('Неправильный формат фамилии')

    def validate_firstname(self, value):
        if re.match('^[А-ЯЁ][а-яё]+', value):
            return value
        return ValidationError('Неправильный формат имени')


    class Meta:
        model = User
        fields = ['id', 'lastname', 'firstname', 'weigth', 'age']
