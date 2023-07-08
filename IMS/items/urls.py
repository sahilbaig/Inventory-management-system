from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.itemsHome , name= "items-home"),
    path('item-details/<str:id>', views.itemDetails , name= "item-details"),
    path('item-sold/<str:id>', views.itemSold , name= "item-sold"),
    path('item-edit/<str:id>' , views.itemEdit , name= "item-edit"),
    path('sell-item/<str:id>', views.sellItem , name='sell-items'),
    path('create-item', views.createItem , name='create-items'),
    path('add-item/<str:id>', views.addItem , name='add-item'),
    path('transactions/<str:id>', views.itemTransactions , name='transactions-item'),
]
