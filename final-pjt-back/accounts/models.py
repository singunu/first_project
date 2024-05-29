from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from financial.models import DepositProducts, SavingProducts
import uuid

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True)
    favorite_deposit_products = models.ManyToManyField(DepositProducts, related_name='favorited_by')
    favorite_saving_products = models.ManyToManyField(SavingProducts, related_name='favorited_by')
    def __str__(self):
        return self.username
    
class TokenModel(models.Model):
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='custom_auth_token',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.key)