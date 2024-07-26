from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.9)

    def __str__(self):
        return self.title
