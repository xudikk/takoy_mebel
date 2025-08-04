from django.db import models
from django.utils.translation import gettext_lazy as _

from dashboard.auth_model import User


# Create your models here.

class Img(models.Model):
    img = models.ImageField(upload_to='media')


class Category(models.Model):
    name = models.CharField(_("Category nomi"), max_length=50)
    length = models.IntegerField(_("Uzinligi"))
    width = models.IntegerField(_("Eni"))
    height = models.IntegerField(_("Balanligi"))
    active = models.BooleanField(default=False, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(_("Product nomi"), max_length=50)
    img = models.ManyToManyField(Img, verbose_name=_("product_img"))
    price = models.IntegerField(_("Product narhi"))
    category = models.ManyToManyField(Category, verbose_name=_("product_category"))
    filling = models.CharField(_("To'ldiradegan narsa"), max_length=250)
    extra = models.JSONField(_("Extra fields"), default=dict)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cart')
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0, editable=False)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.get_price() * self.quantity
        return super(Cart, self).save(*args, **kwargs)


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlist_product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_widhlist')
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.get_price() * self.quantity
        return super(Wishlist, self).save(*args, **kwargs)
