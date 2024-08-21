from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Vista principal
    path('premios/', views.premios, name='premios'),
    path('lista/', views.lista, name='lista'),
    path('reservar_numero/', views.reservar_numeros, name='reservar_numero'),
    path('generar_numero_aleatorio/', views.generar_numero_aleatorio, name='generar_numero_aleatorio'),
    path('verificar_numeros_pagados/', views.verificar_numeros_pagados, name='verificar_numeros_pagados'),
    path('Metodos_de_pago/', views.Metodos_de_pago, name='Metodos_de_pago'),

]
