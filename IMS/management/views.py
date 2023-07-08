from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
import os 
import json


# Create your views here.
def managementHome(request):
    try: 
        with open(("C:/Users/sahil/Desktop/IMS/IMS/management/test.json")) as file:
            data = json.load(file)
    except:
        data = {}
    # jsonData = json.dumps(data)

    context={
        "data" : data
    }

    return render(request,'management/home.html', context)