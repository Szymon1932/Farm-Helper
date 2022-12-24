from django.shortcuts import render, redirect
from ..models import ClassField
from ..forms import CreateClassField
from django.http import HttpResponse


def show_class_fields(request):
    class_fields = ClassField.objects.all()
    return render(request, 'fields/show/classField.html', {'class_fields': class_fields})


def index(request):
    return render(request, 'fields/index.html')
