"""Contains custom widgets for products app"""
from django.forms.widgets import ClearableFileInput, DateInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """Overrides the default ClearableFileInput widget

    Args:
        ClearableFileInput (class): default widget
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html'
    )


class MyDateInput(DateInput):
    "Custom DateInput widget"
    input_type = 'date'
