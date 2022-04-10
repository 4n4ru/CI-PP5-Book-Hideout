# Imports:
# 3rd party:
from django import forms

# Internal:
from .models import Genre, Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genres]

        self.fields['genre'].choices = friendly_names
        for field_name, field in self. fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
