from django.shortcuts import render
from .models import pasteleria
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms 
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def pastelListar(request):
    pasteles= pasteleria.objects.all()
    template="pasteleria/listar.html"
    context={
        'pasteles': pasteles,

    }
    return render (request,template,context)

def pastelCrear(request): 
    if request.method=='POST':
        form= agregar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pastelListar')

    form = agregar 
    context={
        'form':form,

    }
    return render (request, "pasteleria/agregar.html", context)

def pastEliminar(request, id):
  member = pasteleria.objects.get(id=id)
  member.delete()
  return redirect('pastelListar')

def pastActualizar(request, id):
    if request.method=='POST':
        instance=pasteleria.objects.get(id=id)
        form=agregar(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('pastelListar')
    
    dato = pasteleria.objects.get(id=id)
    #form= agregar()
    #form=mymember
    template = 'pasteleria/actualizar.html'
    context = {
    'dato': dato,
    #'form':form,
    }
    return render(request, template, context)