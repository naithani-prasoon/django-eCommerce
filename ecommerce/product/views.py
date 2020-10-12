from django.shortcuts import render

from .models import Products

def productPage(request):
    product = Products.objects.all()
    return render(request, 'product.html', {'prodcuts': product})
