from django import forms
from training.models import Training
from django.core.exceptions import ValidationError


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['exercise', 'weight', 'number', 'user', 'date']

    def clean_weight(self):
        if self.cleaned_data['weight'] >= 0:
            return self.cleaned_data['weight']
        raise ValidationError('Вес отягощения не может быть отрицательным')

    def clean_number(self):
        if self.cleaned_data['number'] >= 0:
            return self.cleaned_data['number']
        raise ValidationError('Число повторений не может быть отрицательным')
