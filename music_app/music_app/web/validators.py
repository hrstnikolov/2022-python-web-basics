import re

from django.core.exceptions import ValidationError


def validate_alphanumeric(value):
    match = re.match(pattern=r'^\w+$', string=value)
    if not match:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')
