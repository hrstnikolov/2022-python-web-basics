from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.core.model_mixins import StrFromFieldsMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_lt_5mb


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'description',)
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='mediafiles/pet-photos/',
        validators=(validate_file_lt_5mb,),
        blank=True,
        null=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        blank=False,
        null=False,
    )

    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )
