
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class RegisterUserForm(UserCreationForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        #fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
        # self['username'].help_text = 'Wymagana. 150 znaków lub mniej. Tylko litery, cyfry i @/./+/-/_.'
        
        # self['password1'].help_text = 'Twoje hasło nie może być zbyt podobne do innych Twoich danych osobowych. \n Twoje hasło musi zawierać co najmniej 8 znaków. Twoje hasło nie może być powszechnie używanym hasłem. Twoje hasło nie może składać się wyłącznie z cyfr.'
        # self['password2'].help_text = ''
    

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
