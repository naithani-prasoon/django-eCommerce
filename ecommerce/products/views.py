from django.shortcuts import render

from .models import Products, Category

def productPage(request):
    total_products = Products.objects.all()
    all_category = Category.objects.all()
    return render(request, 'products.html', {'products': total_products , 'category' : all_category})