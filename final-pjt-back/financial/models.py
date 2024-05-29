from django.db import models
from django.conf import settings

class DepositProducts(models.Model):
    fin_prdt_cd = models.CharField(max_length=100, unique=True)
    kor_co_nm = models.CharField(max_length=100)
    fin_prdt_nm = models.CharField(max_length=100)
    etc_note = models.TextField(null=True, blank=True)
    join_deny = models.IntegerField(null=True, blank=True)
    join_member = models.CharField(max_length=100)
    join_way = models.CharField(max_length=100)
    spcl_cnd = models.TextField(null=True, blank=True)
    min_deposit_amount = models.FloatField(default=0)
    max_deposit_amount = models.FloatField(default=10000000000000.0)
    min_period = models.IntegerField(default=0)
    max_period = models.IntegerField(default=9999)

class SavingProducts(models.Model):
    fin_prdt_cd = models.CharField(max_length=100, unique=True)
    kor_co_nm = models.CharField(max_length=100)
    fin_prdt_nm = models.CharField(max_length=100)
    etc_note = models.TextField(null=True, blank=True)
    join_deny = models.IntegerField(null=True, blank=True)
    join_member = models.CharField(max_length=100)
    join_way = models.CharField(max_length=100)
    spcl_cnd = models.TextField(null=True, blank=True)
    min_deposit_amount = models.FloatField(default=0)
    max_deposit_amount = models.FloatField(default=10000000000000.0)
    min_period = models.IntegerField(default=0)
    max_period = models.IntegerField(default=9999)

class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_tpye_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()


class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_tpye_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()
    rsrv_type = models.TextField()
    rsrv_type_nm = models.CharField(max_length=100)

class FavoriteDepositProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    deposit_product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'deposit_product')

class FavoriteSavingProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    saving_product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'saving_product')