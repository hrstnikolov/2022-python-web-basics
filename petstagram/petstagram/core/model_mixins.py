class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        return ', '.join(f'{field}={getattr(self, field, None)}' for field in self.str_fields)
