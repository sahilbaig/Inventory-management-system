from django.db import models
from items.models import Inventory
from datetime import datetime
# Create your models here.
class Transactions(models.Model):
    name = models.CharField(max_length=100 , default="transaction_name")
    item =  models.ForeignKey(Inventory, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    selling_price = models.PositiveIntegerField()
    transactiondttm=models.DateTimeField(default = datetime.now)