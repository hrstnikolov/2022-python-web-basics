from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_text(text):
    if '_' in text:
        raise ValidationError('`_` is invalid character for `text`.')


def validate_priority(priority):
    if priority < 1 or 10 < priority:
        raise ValidationError('Priority shall be between 1-10.')


class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValidationError(f'Priority shall be between {self.min_value}-{self.max_value}.')


@deconstructible
class ValueInRangeValidatorForForms:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValidationError(f'Priority shall be between {self.min_value}-{self.max_value}.')

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.min_value == other.min_value
            and self.max_value == other.max_value
        )