from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.FloatField(validators=[MinValueValidator(0.01)])
    supplier = models.CharField(max_length=50)

    def __str__(self):
        return self.name
