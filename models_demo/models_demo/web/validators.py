import datetime

from django.core.exceptions import ValidationError


def validate_after_today(date):
    if date < datetime.date.today():
        raise ValidationError(f'The date {date} is before today.')

