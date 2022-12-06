from django import forms
from .models import *


class CreateFertilizer(forms.ModelForm):

    class Meta:
        model = Fertilizer
        fields = '__all__'


class CreateClassField(forms.ModelForm):

    class Meta:
        model = ClassField
        fields = '__all__'


class CreatePlant(forms.ModelForm):

    class Meta:
        model = Plant
        fields = '__all__'
