from django.shortcuts import render, redirect
from .models import Reserva
from django.contrib import messages
import random
from django.http import JsonResponse


def premios(request):
    return render(request, 'home/premios.html')


def Metodos_de_pago(request):
    return render(request, 'home/Metodos_de_pago.html')


def index(request):
    return render(request, 'home/index.html')


def lista(request):
    numeros_reservados = [reserva.numero for reserva in Reserva.objects.all()]

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        numero_celular = request.POST.get('numero_celular')
        cantidad = int(request.POST.get('cantidad', 0))
        numeros = [request.POST.get(f'numero_{i}') for i in range(cantidad)]

        # Verificar si el número de celular ya tiene 6 reservas
        cantidad_reservada = Reserva.objects.filter(numero_celular=numero_celular).count()
        errores = []

        if cantidad_reservada >= 6:
            errores.append('Ya has reservado el máximo de 6 números.')
        else:
            if not nombre or not apellidos or not numero_celular:
                errores.append('Todos los campos son obligatorios.')
            elif any(not num for num in numeros):
                errores.append('Todos los números son obligatorios.')
            elif any(int(num) in numeros_reservados for num in numeros):
                errores.append('Algunos de los números ya están reservados.')
            else:
                for numero in numeros:
                    Reserva.objects.create(
                        nombre=nombre,
                        apellidos=apellidos,
                        numero_celular=numero_celular,
                        numero=int(numero)
                    )
                return redirect('lista')

        context = {
            'errores': errores,
            'numeros': range(60000),  # Rango de números disponibles
            'numeros_reservados': numeros_reservados,
            'numero_aleatorio': random.randint(0, 59999),
        }
        return render(request, 'home/lista.html', context)

    context = {
        'numeros': range(60000),  # Rango de números disponibles
        'numeros_reservados': numeros_reservados,
        'numero_aleatorio': random.randint(0, 59999),
    }
    return render(request, 'home/lista.html', context)


def generar_numero_aleatorio(request):
    total_numeros = set(range(60000))
    numeros_reservados = set(Reserva.objects.values_list('numero', flat=True))
    numeros_disponibles = list(total_numeros - numeros_reservados)

    if numeros_disponibles:
        numero = random.choice(numeros_disponibles)
        return JsonResponse({'numero': numero})
    else:
        return JsonResponse({'error': 'No hay números disponibles'}, status=400)


def verificar_numeros_pagados(request):
    telefono = request.GET.get('telefono')
    numeros_pagados = Reserva.objects.filter(numero_celular=telefono, pagado=True).values_list('numero', flat=True)
    numeros_reservados = Reserva.objects.filter(numero_celular=telefono, pagado=False).values_list('numero', flat=True)

    return JsonResponse({
        'numeros_pagados': list(numeros_pagados),
        'numeros_reservados': list(numeros_reservados),
    })


def reservar_numeros(request):
    if request.method == 'POST':
        telefono = request.POST.get('numero_celular')
        cantidad_reservada = Reserva.objects.filter(numero_celular=telefono).count()

        if cantidad_reservada >= 6:
            return render(request, 'home/lista.html', {'errores': ['Ya has reservado el máximo de 6 números.']})

        # Continuar con la lógica de reserva si no se ha alcanzado el límite
        cantidad_a_apartar = int(request.POST.get('cantidad'))
        # Lógica para apartar los números
        # ...

        # Redirigir o mostrar un mensaje de éxito
        return redirect('lista')
    else:
        # Si no es un POST request, renderizar la página normalmente
        return render(request, 'home/lista.html')
