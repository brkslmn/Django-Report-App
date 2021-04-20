from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customers', default='157-1579943_no-profile-picture-round')

    def __str__(self):
        return str(self.name)
    