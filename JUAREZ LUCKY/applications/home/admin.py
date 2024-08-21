from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'numero_celular', 'numero', 'pagado')
    list_filter = ('pagado',)
    search_fields = ('nombre', 'apellidos', 'numero_celular', 'numero')
    actions = ['marcar_como_pagado']

    def marcar_como_pagado(self, request, queryset):
        queryset.update(pagado=True)
    marcar_como_pagado.short_description = "Marcar como pagado"
_description = "Marcar seleccionados como pagados"