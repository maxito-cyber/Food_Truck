from django.shortcuts import render
from .models import Producto
# Create your views here.
def catalogo(request):
    productos = Producto.objects.all()
    return render(request,
                "pedidos/catalogo.html",
                {"productos": productos}) 
