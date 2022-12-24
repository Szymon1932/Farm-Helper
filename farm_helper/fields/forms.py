
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
        self.fields['username'].label='Nazwa użytkownika'
        self.fields['password1'].label='Hasło'
        self.fields['password2'].label='Powtórz hasło'
    

class CreateFertilizer(forms.ModelForm):

    class Meta:
        model = Fertilizer
        fields = '__all__'
        labels = {
            'fertilizer_name': 'Nazwa nawozu',
            'price': 'Cena za tonę',
        }


class CreateClassField(forms.ModelForm):
    class Meta:
        model = ClassField
        fields = '__all__'
        


class CreatePlant(forms.ModelForm):

    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_name': 'Nazwa rośliny',
            'seed_price': 'Cena za tonę',
        }

DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d')


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class CreatePlantPrice(forms.ModelForm):
    date = forms.DateField(widget=DatePickerInput)

    class Meta:
        model = PlantPrice
        fields = ('price', 'date', 'plant')
    def __init__(self, *args, **kwargs):
        super(CreatePlantPrice, self).__init__(*args, **kwargs)
        self.fields['price'].label='Cena rośliny'
        self.fields['date'].label='Data'
        self.fields['plant'].label='Roślina'


class CreatePredictedCrop(forms.ModelForm):

    class Meta:
        model = PredictedCrop
        fields = '__all__'
        labels = {
            'predicted_crop_name': 'Nazwa przewidywanego plonu',
            'plant': 'Nazwa rośliny',
            'crop_mass': 'Masa plonu (t)',
            'class_field': 'Klasa ziemi',
        }

class CreateFertilizationPlan(forms.ModelForm):

    class Meta:
        model = FertilizationPlan
        fields = '__all__'
        labels = {
            'predicted_crop': 'Nazwa przewidywanego plonu',
            'fertilizer': 'Nazwa nawozu',
            'fertilizer_mass': 'masa nawozu (t)',
        }

class CreateField(forms.ModelForm):

    class Meta:
        model = Field
        fields = ('field_name','area','class_field')
        labels = {
            'field_name': 'Nazwa pola',
            'area': 'Powierzchnia (ha)',
            'class_field': 'Klasa ziemi',
        }