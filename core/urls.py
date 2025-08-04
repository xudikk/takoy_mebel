from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/", views.catalog, name="catalog"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("cart/", views.cart, name="cart"),
    path("compare/", views.compare, name="compare"),
    path("contacts/", views.contacts, name="contacts"),
]
