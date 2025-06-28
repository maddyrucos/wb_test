from django.db import models

class Product(models.Model):
    nm_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    price_basic = models.FloatField()
    price_basic_rub = models.FloatField()
    price_total = models.FloatField()
    price_total_rub = models.FloatField()
    rating = models.FloatField()
    feedbacks = models.IntegerField()
    
    @property
    def discount_percent(self):
        if self.price_basic == 0:
            return 0
        return round((self.price_basic - self.price_total) / self.price_basic * 100, 2)


    def __str__(self):
        return self.name