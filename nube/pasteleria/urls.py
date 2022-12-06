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
    path('pasteleria/listar/', pastelListar, name='pastelListar'),
    path('pasteleria/crear/', pastelCrear, name='pastelCrear'),
    path('pasteleria/eliminar/<int:id>', pastEliminar, name='pastEliminar'),
    path('pasteleria/actualizar/<int:id>', pastActualizar, name='pastActualizar'),
]