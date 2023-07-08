from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Transactions
from items.models import Inventory

# Create your views here.
def transaction(request,id):
    item = Inventory.objects.filter(id=id)
    transactions=  Transactions.objects.filter(item= item)
    return JsonResponse({
        "status":200,
        "content": "Transaction success"
    })

