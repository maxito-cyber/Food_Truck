from django.shortcuts import render
from django.http import httpResponse
from .models import Producto
# Create your views here.
def catalgo(request):
    productos = Producto.objects.all()
    texto = "catalogo\n\n"
    for p in productos:
        texto += f"{p.nombre} - "
        texto += f"{p.categoria.nombre}\n"
    return httpResponse(texto,
        content_type="text/plaain; charset=utf-8")