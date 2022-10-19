from django.db import models
from django.utils.text import slugify

from petstagram.core.model_mixins import StrFromFieldsMixin


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name',)
    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        blank=False,
        null=False,
    )
    personal_photo = models.URLField(
        blank=False,
        null=False,
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        return super().save(*args, **kwargs)
