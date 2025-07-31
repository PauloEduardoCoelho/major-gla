from django.contrib import admin
from .models import Ilha, Informacao

@admin.register(Ilha)
class IlhaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Informacao)
class InformacaoAdmin(admin.ModelAdmin):
    list_display = ['ilha', 'categoria']
    list_filter = ['ilha', 'categoria']
    search_fields = ['ponto_referencia']
