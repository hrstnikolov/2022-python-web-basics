from django.core.exceptions import ValidationError

from petstagram.core.utils import megabytes_to_bytes


def validate_file_lt_5mb(field_file_obj):
    filesize = field_file_obj.file.size
    megabyte_limit = 5
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f"Maximum file size: {megabyte_limit}MB")
