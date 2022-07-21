from django.shortcuts import (get_object_or_404,
                              render,
                              redirect,
                              HttpResponseRedirect)
from django.contrib import messages
from django.http import HttpResponse
from dbc.models import InsertToDb
from .resources import PersonResource
from tablib import Dataset
from dbc.forms import PersonData
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from . import forms


def save_to_db(request):
    if request.method == "POST":
        name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone_number"]
        ins = InsertToDb(first_name=name, last_name=last_name, email=email, phone_number=phone)
        
        ins.save()
        print("The data has been written to db")
        # print(name, last_name, email, phone)
        # foo_instance = Contact.objects.create(name=name)
        messages.success(request, 'Form submission successful')
    return render(request, "form.html")

# def view_info(request):
    

def delete(request, id):
    form_entry = InsertToDb.objects.get(id=id)
    form_entry.delete()
    return redirect("/display")

# def edit(request, id):
#     form = InsertToDb.objects.get(id=id)
#     some_form = PersonData(request.POST, instance=form)
#     if some_form.is_valid():
#         some_form.save()
#         # return redirect("/form/display/")
#     return render(request, 'edit.html', {'form':form})

def edit(request, id=None):
    form = InsertToDb.objects.get(pk=id)
    some_form = PersonData(request.POST, instance=form)
    if some_form.is_valid():
        some_form.save()
        return redirect("/display")
    return render(request, 'edit.html', {'form':form})
   

# def update(request, id):
#     update_d = InsertToDb.objects.get(id=id)
    
#         return render(request, "edit.html", {'form':update_d})


def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response

def simple_upload(request):
    objs=InsertToDb.objects.all()
    # return render(request,'show_in_table.html',{'objs':objs})
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read(),format='xlsx')
        print(imported_data)
        for data in imported_data:
        	value = InsertToDb(
        		data[0],
        		data[1],
        		data[2],
                data[3],
                data[4]
        		)
        	value.save()
        return redirect("/display") 

    return render(request, 'show_in_table.html', {'objs':objs})



