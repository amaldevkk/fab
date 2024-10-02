from django.db import models

# Create your models here.
# models.py



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name




