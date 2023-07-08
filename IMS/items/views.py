from django.http import JsonResponse
from django.shortcuts import render, redirect
from items.models import Inventory
from transactions.models import Transactions

item_home  = "/items/"

def itemsHome(request):
    items=Inventory.objects.all().values()
    context = {
        'items': items,
    }
    return render(request,'items/home.html' , context )


def itemDetails(request, id):
    items=Inventory.objects.filter(IIN=id)
    context = {
        'items': items
    }
    return render(request , 'items/itemDetails.html' , context)

def itemSold(request):
    
    return render(request , 'items/itemSold.html')

def itemEdit(request, id):
    items=Inventory.objects.filter(IIN=id).values()
    context ={
        "items": items[0]
    }


    if request.method=="POST":
        updated_name = request.POST.get('item-name')
        updated_selling_price=request.POST.get('item-selling-price')
    
        updated_item=Inventory.objects.filter(IIN=id)
        updated_item.update(name=updated_name , selling_price = updated_selling_price)

        return redirect(item_home)
    elif request.method =="GET":
        pass

    return render(request, 'items/itemEdit.html' , context)

def sellItem(request , id):
    if request.method == "POST":
        items=Inventory.objects.filter(IIN=id).first()
        quantity = request.POST.get('item-quantity')  
        items.quantity = items.quantity- int(quantity)
        items.save()
        transaction = Transactions(quantity=quantity , selling_price= items.selling_price , item = items )
        transaction.save()

        return redirect(item_home)

    return render (request , 'items/itemSell.html')

def createItem(request):
    if request.method=="POST":
        name = request.POST.get('item-name')
        IIN = request.POST.get('IIN')
        cost= request.POST.get('cost')
        quantity = request.POST.get('quantity')
        selling_price = request.POST.get('selling-price')
        created_item=Inventory(name= name, IIN= IIN ,cost = cost , quantity = quantity , selling_price =selling_price )
        created_item.save()
        return redirect(item_home)
    return render(request, 'items/itemCreate.html')


def addItem(request, id):
    if request.method=="POST":
        item = Inventory.objects.filter(id=id).first()
        quantity = request.POST.get('item-quantity')
        item.quantity = item.quantity + int(quantity)
        item.save()
        return redirect(item_home)
    return render(request , 'items/itemAdd.html')    

def itemTransactions(request, id):
    item = Inventory.objects.filter(id=id).first()
    transactions = Transactions.objects.filter(item = item)
    context= {
        "transactions": transactions
    }
    return render(request ,  'items/itemTransactions.html' , context)