from django.db import models

class task(models.Model):
    name = models.CharField(
        max_length=30,
        null=False,
    )

    description = models.TextField()