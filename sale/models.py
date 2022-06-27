# Imports:
# 3rd party:
from django.db import models
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
    start_date = models.DateField()
    end_date = models.DateField(
        validators=[date_not_in_past],
    )
    books = models.ManyToManyField(
        Product,
    )

    def __str__(self):
        return f'{self.name}'

    def clean(self):
        super().clean()
        if not (self.start_date < self.end_date):
            raise ValidationError({'end_date': [
                'The end date needs to be after the start date.'
            ], })

        sales = Sale.objects.all()
        for sale in sales:
            start_date = sale.start_date
            end_date = sale.end_date
            if (self.start_date >= start_date and self.start_date <= end_date):
                raise ValidationError({'start_date': [
                    f'You already have a sale ({sale}) during this period.'
                ], })
            elif (self.end_date >= start_date and self.end_date <= end_date):
                raise ValidationError({'end_date': [
                    f'You already have a sale ({sale}) during this period.'
                ], })
