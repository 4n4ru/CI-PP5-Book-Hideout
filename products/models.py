"""
Models for the products app
"""

from django.db import models
from django.core.validators import MinLengthValidator


class Genre(models.Model):
    """
    Class for the genre model
    """
    name = models.CharField(
        max_length=254
    )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        """Returns the genres name as a string

        Returns:
            string: genre name
        """
        return f'{self.name}'

    def get_friendly_name(self):
        """Retruns the genres front end friendly name

        Returns:
            string: front end friendly name
        """
        return self.friendly_name


class Product(models.Model):
    """
    Class for the product model
    """
    genre = models.ManyToManyField(
        'Genre',
        blank=True,
    )
    isbn = models.CharField(
        max_length=10,
    )
    isbn13 = models.CharField(
        max_length=13,
    )
    title = models.CharField(
        max_length=254
    )
    subtitle = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    authors = models.CharField(
        max_length=254
    )
    description = models.TextField()
    publisher = models.CharField(
        max_length=254
    )
    publication_date = models.DateField()
    format = models.CharField(
        max_length=254
    )
    pages = models.IntegerField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1
    )
    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )

    def __str__(self):
        """Returns the products title as a string

        Returns:
            string: title
        """
        return f'{self.title}'
