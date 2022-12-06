from django.contrib import admin
from django.urls import path
from .views import*
import re
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from .views import *



urlpatterns = [
    path('prueba/listar/',listar,name="listar"),
    path('prueba/crear/', carrocrear, name='crear'),
    path('prueba/eliminar/<int:id>',eliminar,name='eliminar'),
    path('prueba/actualizar/<int:id>',actualizar,name='actualizar'),
]