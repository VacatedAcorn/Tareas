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
    path('pizzeria/listar/',pizzaListar,name="listar"),
    path('pizzeria/crear/', pizzaCrear, name='crear'),
    path('pizzeria/eliminar/<int:id>',pizzaEliminar,name='eliminar'),
    path('pizzeria/actualizar/<int:id>',pizzaActualizar,name='actualizar'),
]