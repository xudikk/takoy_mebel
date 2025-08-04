
from django.shortcuts import render, get_object_or_404
from .models import Product, Customer, Order, OrderItem, Review

# Create your views here.


def index(request):
    products = Product.objects.all()[:6]
    return render(request, "index.html", {"products": products})

def catalog(request):
    products = Product.objects.all()
    return render(request, "catalog.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    return render(request, "product.html", {"product": product, "reviews": reviews})

def cart(request):
    orders = Order.objects.all()
    return render(request, "cart.html", {"orders": orders})

def compare(request):
    products = Product.objects.all()[:2]
    return render(request, "compare.html", {"products": products})

def contacts(request):
    return render(request, "contacts.html")
