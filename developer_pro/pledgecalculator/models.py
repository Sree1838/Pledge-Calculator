from django.db import models

# Create your models here.
class Stock_details(models.Model):
    stock_name = models.CharField(max_length=100)
    n_shares = models.IntegerField()
    def __str__(self):
        return self.stock_name
