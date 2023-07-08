from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    IIN = models.CharField(unique=True, max_length=100)
    cost = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    quantity_sold  = models.PositiveIntegerField(default=0)
    selling_price  = models.PositiveIntegerField()
    profit_earned = models.PositiveIntegerField(default=0)
    revenue = models.PositiveIntegerField(default=0)
    
