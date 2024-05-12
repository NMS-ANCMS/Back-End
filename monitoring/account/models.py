from django.contrib.auth.models import AbstractUser
from django.db import models
import pyotp

# Create your models here.

class User(AbstractUser):
    avatar = models.CharField(max_length=20, verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    otp = models.CharField(max_length=6)
    is_two_factor_authentication_enabled = False

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()


