from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from products.models import Products

User = get_user_model()

class CartItem(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE)
    this_cart_key = models.ForeignKey('Cart',  null = True, blank = True, on_delete = models.CASCADE)
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1, null = True)
    ordered_time = models.DateTimeField(auto_now_add = True, auto_now = False)
    update = models.DateTimeField(auto_now_add = False, auto_now = True)

    def __str__(self):
        return(self.product.title)

class Cart(models.Model):
    items_in_cart = models.ManyToManyField(CartItem, related_name= 'CART')
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE)