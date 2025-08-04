from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=123)
    is_menu = models.BooleanField(default=False)
    slug = models.SlugField(max_length=123)
    is_deleted = models.BooleanField(default=False)


    def get_response(self):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "is_deleted": self.is_deleted

        }


    def deleted(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()
        self.ctg_products.all().delete()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class CustomManager(models.Model):
        def all(self):
            return self.get_queryset().filter(is_deleted=False)

        def get(self, *args, **kwargs):
            return self.model.get_queryset().filter(is_deleted=False, *args, **kwargs).first()

    objects = CustomManager()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)
    price_type = models.CharField(max_length=3, choices=[
        ("UZS", "Ozbek somi"),
    ], default="UZS")
    discount = models.IntegerField(default=20)
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="ctg_products")


def get_price(self):
    if self.discount > 0:
        return round(self.price * (1 - (self.discount / 100)), 2)
    return self.price


def get_price_with_icon(self):
    symbols = {

        "UZS": "So'm"
    }
    return f"{symbols.get(self.price_type, '')}{self.get_price()}"

def mark_as_deleted(self):
    self.deleted = True
    self.save(update_fields=["deleted"])

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    related_carts = getattr(self, "cart_pro", None)
    if related_carts:
        for cart_item in related_carts.all():
            cart_item.save()


class Customer(models.Model):
    user = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"{self.user} ({self.email})"

    def get_full_info(self):
        return f"Name: {self.user}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"

    def get_phone_number(self):
        if not self.phone.startswith("+998"):
            return f"+998 {self.phone}"
        return self.phone

    def get_email_domain(self):
        return self.email.split("@")[-1]


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Kutilmoqda"), ("shipped", "Jo‘natilgan"), ("delivered", "Yetkazilgan")],
        default="pending"
    )

    def __str__(self):
        return f"Order #{self.id} - {self.customer.user} ({self.status})"

    def get_order_date(self):
        return self.created_at.strftime("%d-%m-%Y %H:%M")

    def get_status_display_uz(self):
        status_dict = {
            "pending": "Kutilmoqda",
            "shipped": "Jo‘natilgan",
            "delivered": "Yetkazilgan"
        }
        return status_dict.get(self.status, "Noma’lum")

    def is_active(self):
        return self.status in ["pending", "shipped"]


    def get_customer_name(self):
        return self.customer.user



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_price(self):
        return self.product.price

    def get_total_price(self):
        return self.product.price * self.quantity

    def get_product_name(self):
        return self.product.name

    def get_order_id(self):
        return self.order.id


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField(default=5)  # 1 dan 5 gacha
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer.user} - {self.rating}⭐"


    def short_comment(self):
        if self.comment:
            return self.comment[:30] + ("..." if len(self.comment) > 30 else "")
        return "Izoh yo‘q"


    def stars(self):
        return "⭐" * self.rating + "☆" * (5 - self.rating)


    def get_review_date(self):
        return self.created_at.strftime("%d-%m-%Y %H:%M")


    def get_customer_name(self):
        return self.customer.user


    def get_product_name(self):
        return self.product.name










