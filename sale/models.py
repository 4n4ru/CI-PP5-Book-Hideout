# Imports:
# 3rd party:
from django.db import models

# Internal:
from products.models import Product


class Sale(models.Model):
    percentage = models.DecimalField(
        max_digits=2,
        decimal_places=0,
    )
    start_date = models.DateField()
    end_date = models.DateField()
    books = models.ManyToManyField(
        Product,
    )

    def __str__(self):
        return f'{self.percentage}% Sale'
