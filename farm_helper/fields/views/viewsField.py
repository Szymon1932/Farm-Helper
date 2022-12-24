from django.shortcuts import render, redirect
from ..models import *
from ..forms import *
from django.http import HttpResponse
from django.contrib import messages

def show_fields(request):
    fields = Field.objects.filter(user = request.user.id)
    return render(request, 'fields/show/field.html', {'fields': fields})


def index(request):
    return render(request, 'fields/index.html')


def add_field(request):
    add_field = CreateField()
    if request.method == 'POST':
        add_field = CreateField(request.POST, request.FILES)
        if add_field.is_valid():
            if(add_field.cleaned_data['area']>0):
                field = Field.objects.create(
                        field_name = add_field.cleaned_data['field_name'],
                        area = add_field.cleaned_data["area"],
                        user = request.user.id,
                        class_field = add_field.cleaned_data["class_field"],
                    )
                field.save()
                return redirect('show-fields')
            else:
                messages.success(request, ("Błąd podczas wprowadzania danych"))
                return redirect('show-fields')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-fields')
    else:
        return render(request, 'fields/add/addField.html', {'upload_form': add_field})


def update_field(request, field_id):
    field_id = int(field_id)
    try:
        field_obj = Field.objects.get(id=field_id)
    except Field.DoesNotExist:
        return redirect('show-fields')
    field_form = CreateField(
        request.POST or None, instance=field_obj)
    if field_form.is_valid():
        if(field_form.cleaned_data['area']>0):
            field_form.save()
            return redirect('show-fields')
        else:
            messages.success(request, ("Błąd podczas wprowadzania danych"))
            return redirect('show-fields')
    return render(request, 'fields/add/addField.html', {'upload_form': field_form})


def delete_field(request, field_id):
    field_id = int(field_id)
    try:
        field_obj = Field.objects.get(id=field_id)
    except Field.DoesNotExist:
        return redirect('show-fields')
    field_obj.delete()
    return redirect('show-fields')
