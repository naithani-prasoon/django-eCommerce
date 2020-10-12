from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=25)
    offer = models.BooleanField(default=False)
    category = models.CharField(max_length=25)
    descirption = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    discount_price = models.IntegerField(default=0)
    image = models.ImageField()

    class Meta:
        managed = True

    def __str__(self):
        return self.title

