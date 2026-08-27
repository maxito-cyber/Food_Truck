from django.contrib import admin
from .models import Categoria, Producto, Cliente, Pedido, Detallepedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nombre",)
    search_fileds=("nombre",)


@admin.register(Producto)
class ProductorAdmin(admin.ModelAdmin):
    LIST_DISPLAY = {"nombre", "precio", "categoria"}
    search_fields = {"nombre",}
    list_filter = {"categoria",}
    ordering = ("nombre",)
