from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'peca', 'status', 'data_retirada', 'data_devolucao', 'valor_total']
    search_fields = ['cliente__nome', 'peca__nome']
    list_filter = ['status']