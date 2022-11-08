from django.db import models

from petstagram.photos.models import Photo


class PhotoComment(models.Model):
    class Meta:
        ordering = ['-publication_datetime']

    MAX_COMMENT_LENGTH = 300

    text = models.CharField(
        max_length=MAX_COMMENT_LENGTH,
        null=False,
        blank=False,
    )

    publication_datetime = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
        editable=False,
    )

    photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    to_photo = models.ForeignKey(
        to=Photo,
        on_delete=models.CASCADE,
    )

    # TODO: to be implemented when auth
    # user = models.ForeignKey(
    #     to=User,
    # )
