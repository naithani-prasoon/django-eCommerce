from django.db import models

class Featured(models.Model):
    image = models.ImageField(upload_to = 'featured_static/', blank = True)

    class Meta:
        managed = True
    


