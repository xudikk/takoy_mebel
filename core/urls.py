











from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('catalog', catalog, name="catalog"),
    path('compare', compare, name="compare"),
    path('product', product, name="product"),
    path('cart', cart, name="cart"),
    path('contacts', contacts, name="contacts"),
]
