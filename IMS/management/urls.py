from django.urls import path
from . import views
urlpatterns = [
    path('', views.managementHome , name= "management-home")
]
