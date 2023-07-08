from django.db import models
from items.models import Inventory 
 
# Create your models here.
class Orders(models.Model):
    name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    item = models.ForeignKey(Inventory, on_delete = models.CASCADE)
    is_recieved = models.BooleanField(default=None, blank=True, null=True)
    is_cancelled = models.BooleanField(default=None, blank=True, null=True)
   
    
