# Imports:
# 3rd party:
from django import forms

# Internal:
from .models import Sale
from book_hideout.widgets import MyDateInput
from products.models import Product


class SaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = '__all__'

    start_date = forms.DateField(
        widget=MyDateInput(),
    )

    end_date = forms.DateField(
        widget=MyDateInput(),
    )

    books = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black rounded-0'
