from datetime import date
from django.core.exceptions import ValidationError

def date_not_in_past(date_to_check):
    """Validate if the date to be checked is in the past, if it is, raise
    validation error

    Args:
        date_to_check (datetime.date): Date to be checked

    Raises:
        ValidationError: Notifies the user that the date can't be in the past
    """
    if date_to_check < date.today():
        raise ValidationError("The date cannot be in the past.")
