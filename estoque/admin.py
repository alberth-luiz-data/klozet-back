from django.contrib import admin
from .models import Peca

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nome', 'tamanho', 'cor', 'valor_diaria', 'disponivel']
    search_fields = ['codigo', 'nome']
    list_filter = ['tamanho', 'disponivel']