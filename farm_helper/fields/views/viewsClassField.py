from django.shortcuts import render, redirect
from ..models import ClassField
from ..forms import CreateClassField
from django.http import HttpResponse


def show_class_fields(request):
    class_fields = ClassField.objects.all()
    return render(request, 'fields/show/classField.html', {'class_fields': class_fields})


def index(request):
    return render(request, 'fields/index.html')


def add_class_field(request):
    add_class_field = CreateClassField()
    if request.method == 'POST':
        add_class_field = CreateClassField(request.POST, request.FILES)
        if add_class_field.is_valid():
            add_class_field.save()
            return redirect('show-class_fields')  # name in urls
        else:
            return HttpResponse("""Błędne dane. <a href = "{{ url : 'show-class_fields'}}">Odśwież</a>""")
    else:
        return render(request, 'fields/add/addClassField.html', {'upload_form': add_class_field})


def update_class_field(request, class_field_id):
    class_field_id = int(class_field_id)
    try:
        class_field_obj = ClassField.objects.get(id=class_field_id)
    except ClassField.DoesNotExist:
        return redirect('show-class_fields')
    class_field_form = CreateClassField(
        request.POST or None, instance=class_field_obj)
    if class_field_form.is_valid():
        class_field_form.save()
        return redirect('show-class_fields')
    return render(request, 'fields/add/addClassField.html', {'upload_form': class_field_form})


def delete_class_field(request, class_field_id):
    class_field_id = int(class_field_id)
    try:
        class_field_get = ClassField.objects.get(id=class_field_id)
    except ClassField.DoesNotExist:
        return redirect('show-class_fields')
    class_field_get.delete()
    return redirect('show-class_fields')
