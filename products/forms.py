# Imports:
# 3rd party:
from django import forms

# Internal:
from .models import Genre, Product
from book_hideout.widgets import CustomClearableFileInput, MyDateInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    genre = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    publication_date = forms.DateField(
        widget=MyDateInput(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genres = Genre.objects.all()
        queryset = [(g.id, g.get_friendly_name()) for g in genres]
        self.fields['genre'].choices = queryset
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
        self.fields['isbn'].widget.attrs['pattern'] = r'\d{9}[\dX]'
        self.fields['isbn'].widget.attrs['title'] = 'Please enter a valid \
            ISBN.'
        self.fields['isbn13'].widget.attrs['pattern'] = r'\d{13}'
        self.fields['isbn13'].widget.attrs['title'] = 'Please enter a valid \
            ISBN13.'
