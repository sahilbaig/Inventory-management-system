from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts  = [
    {
        'author':"somebod",
        "title": "soome other title"
    },
    {
        "author": "somebody else",
        "title": "some other title"
    }

]
 
def home(req):
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }   
    return render(req, 'home.html' , context)  

def about(req):
    return HttpResponse('<p>About section </p>')