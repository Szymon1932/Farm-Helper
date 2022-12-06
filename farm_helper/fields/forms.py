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


DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d')


class CreatePlantPrice(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(
        format='%d/%m/%Y'), input_formats=DATE_INPUT_FORMATS)  # add better formatting and filerting
    # add retrieving name not key

    class Meta:
        model = PlantPrice
        fields = '__all__'
