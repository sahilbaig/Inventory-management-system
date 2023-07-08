from django.urls import path , include
from . import views
urlpatterns = [
    path('new', views.ordersNew, name="order-new"),
    path('placed/<int:id>', views.ordersPlaced , name="orders-placed" ),
    path('cancelled/<int:id>' , views.ordersCancelled , name="orders-cancelled"),
    path('recieved/<int:id>' , views.ordersRecieved , name = "orders-recieved" ),
    path('status/<int:id>/<int:orderStatus>' , views.orderStatus , name="order-status")
]