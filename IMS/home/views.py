from django.shortcuts import render
from items.models import Inventory
from django.db.models import Max

# Create your views here.
def homeScreen (request):
    max_cost = Inventory.objects.all().annotate(max_cost=Max("cost"))
    max_profit = Inventory.objects.all().annotate(max_profit=Max("profit_earned"))
    max_sold = Inventory.objects.all().annotate(max_profit=Max("quantity_sold"))
    out_of_stock = Inventory.objects.filter(quantity=0)
    context ={
        "max_cost": max_cost.values(),
        "max_profit" : max_profit.values(),
        "max_sold" : max_sold.values(),
        "out_of_stock": out_of_stock.values(),
        
    }

    return render(request, 'home.html' , context) 
