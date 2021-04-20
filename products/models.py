from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to ='products', default='157-1579943_no-profile-picture-round')
    price = models.FloatField(help_text='in $')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"
    