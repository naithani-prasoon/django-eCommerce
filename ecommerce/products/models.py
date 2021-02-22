from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Products(models.Model):
    title = models.CharField(max_length=25)
    offer = models.BooleanField(default=False)
    category = models.CharField(max_length=25)
    filters = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=100, default='')
    price = models.FloatField(default=0.0)
    discount_price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to = 'product_static/', blank = True)

    class Meta:
        managed = True

    def __str__(self):
        return self.title
