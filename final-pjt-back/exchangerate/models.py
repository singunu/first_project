from django.db import models

class ExchangeRate(models.Model):
    cur_unit = models.CharField(max_length=10)
    cur_nm = models.CharField(max_length=50)
    ttb = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField로 변경
    tts = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField로 변경
    deal_bas_r = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField로 변경
    bkpr = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField로 변경
    yy_efee_r = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField로 변경
    ten_dd_efee_r = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField로 변경
    kftc_deal_bas_r = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField로 변경
    kftc_bkpr = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField로 변경
