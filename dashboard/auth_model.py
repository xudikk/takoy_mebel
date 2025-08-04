from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):
    def create_user(self, phone, password, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(
            phone=phone,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields)

        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, phone, password, is_staff=True, is_superuser=True, **extra_fields):
        return self.create_user(phone=phone, password=password, is_staff=is_staff, is_superuser=is_superuser,
                                **extra_fields)


class User(AbstractUser):
    user_name = models.CharField(_("Ism familiya"), max_length=50)
    phone = models.CharField(_("Telefon raqam"), max_length=50, unique=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.SmallIntegerField(default=1, choices=[
        (1, 'user'),
        (2, 'admin')
    ])

    username = False
    email = False
    first_name = False
    last_name = False

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['user_type']


        
    # def calculate_cart(self):
    #     carts = self.user_cart.filter(status=True)
    #     total_balance = 0
    #     valyuta = {
    #         "USD": 12800,
    #         "RUB": 163,
    #         "UZS": 1
    #     }
    #     for i in carts:
    #         cart_total = i.total_price
    #         price_type = i.product.price_type
    #         total_balance += cart_total * valyuta[price_type]
    #     return f"{total_balance // 12800}"
































