from django import forms
from .models import *


class CreateFertilizer(forms.ModelForm):

    class Meta:
        model = Fertilizer
        fields = '__all__'
        labels = {
            'fertilizer_name': 'Nazwa nawozu',
            'price': 'Cena', #todo zmiana labeli
        }


class CreateClassField(forms.ModelForm):
    class Meta:
        model = ClassField
        fields = '__all__'


class CreatePlant(forms.ModelForm):

    class Meta:
        model = Plant
        fields = '__all__'


DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d')


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class CreatePlantPrice(forms.ModelForm):
    # date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=DATE_INPUT_FORMATS)  # add better formatting and filerting
    date = forms.DateField(widget=DatePickerInput)

    class Meta:
        model = PlantPrice
        fields = '__all__'


class CreatePredictedCrop(forms.ModelForm):

    class Meta:
        model = PredictedCrop
        fields = '__all__'


class CreateFertilizationPlan(forms.ModelForm):

    class Meta:
        model = FertilizationPlan
        fields = '__all__'


class CreateField(forms.ModelForm):

    class Meta:
        model = Field
        fields = '__all__'
