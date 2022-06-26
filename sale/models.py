# Imports:
# 3rd party:
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

# Internal:
from products.models import Product
from .validators import date_not_in_past


class Sale(models.Model):
    name = models.CharField(
        max_length=254,
        unique=True
    )
    percentage = models.DecimalField(
        max_digits=2,
        decimal_places=0
    )
    start_date = models.DateField(
        validators=[date_not_in_past]
    )
    end_date = models.DateField()
    books = models.ManyToManyField(
        Product,
    )

    def __str__(self):
        return f'{self.name}'

    def clean(self):
        super().clean()
        if not (self.start_date < self.end_date):
            raise ValidationError("The end date needs to be after the \
                start date.")
