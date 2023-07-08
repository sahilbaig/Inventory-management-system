from django.shortcuts import render, redirect
from django.http import JsonResponse 
from .models import Orders
from items.models import Inventory

def ordersPlaced(request, id):
    orders = Orders.objects.filter(item__id=id)
    context={
        "orders": orders
    }
    return render(request , 'orders/ordersPlaced.html' , context)

def ordersCancelled(request,id):
    orders = Orders.objects.filter(item__id=id ,is_cancelled =True)
    context={
        "orders": orders
    }

    return render(request , 'orders/ordersCancelled.html' , context)

def ordersRecieved(request , id ):
    orders = Orders.objects.filter(item__id=id ,is_recieved =True)
    context={
        "orders": orders
    }
    return render(request , 'orders/ordersRecieved.html', context)

def ordersNew(request):
    if request.method=="POST":
        orderName = request.POST.get('order-name')
        orderQuantity = request.POST.get('order-quantity')
        orderCost=  request.POST.get('order-cost')
        itemIIN = request.POST.get('item-IIN')
        item  = Inventory.objects.filter(IIN= itemIIN )
        order_created=Orders(name = orderName , quantity= orderQuantity , cost=orderCost , item = item[0] )    
        order_created.save()

    
    return render(request , 'orders/ordersNew.html') 

def orderStatus(request , orderStatus , id):
    orders = Orders.objects.filter(item__id=id)
    orders.update(is_recieved=orderStatus , is_cancelled= not orderStatus)
    
    return redirect('/')