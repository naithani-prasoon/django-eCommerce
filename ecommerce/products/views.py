from django.shortcuts import render

from .models import Products

def productPage(request):
    total_products = Products.objects.all()
    return render(request, 'products.html', {'products': total_products})