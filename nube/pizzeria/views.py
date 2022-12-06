from django.shortcuts import render
from .models import pizzeria
from .forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms 
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def pizzaListar(request):
    pizzas= pizzeria.objects.all()
    template="pizzeria/listar.html"
    context={
        'pizzas': pizzas,

    }
    return render (request,template,context)

def pizzaCrear(request): 
    if request.method=='POST':
        form= agregar(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pizzeria/listar/')

    form = agregar 
    context={
        'form':form,

    }
    return render (request, "pizzeria/agregar.html", context)

def pizzaEliminar(request, id):
  member = pizzeria.objects.get(id=id)
  member.delete()
  return redirect('/pizzeria/listar/')

def pizzaActualizar(request, id):
    if request.method=='POST':
        instance=pizzeria.objects.get(id=id)
        form=agregar(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/pizzeria/listar/')
    
    dato = pizzeria.objects.get(id=id)
    #form= agregar()
    #form=mymember
    template = 'pizzeria/actualizar.html'
    context = {
    'dato': dato,
    #'form':form,
    }
    return render(request, template, context)

# Create your views here.
