from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MAX_LEN_PASSWORD = 30
    MAX_LEN_FIRST_NAME = 30
    MAX_LEN_LAST_NAME = 30

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(12),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name:
            if self.last_name:
                name = f'{self.first_name} {self.last_name}'
            else:
                name = self.first_name
        elif self.last_name:
            name = self.last_name
        else:
            name = None

        return name


class Game(models.Model):
    MAX_LEN_TITLE = 30
    MAX_LEN_CATEGORY = 15
    MIN_RATING = 0.1
    MAX_RATING = 5.0
    MIN_VALUE_MAX_LEVEL = 1

    ACTION_GAME = "Action"
    ADVENTURE_GAME = "Adventure"
    PUZZLE_GAME = "Puzzle"
    STRATEGY_GAME = "Strategy"
    SPORTS_GAME = "Sports"
    BOARD_AND_CARD_GAME = "Board/Card Game"
    OTHER_GAME = "Other"

    GAME_CHOICES = (
        (ACTION_GAME, ACTION_GAME),
        (ADVENTURE_GAME, ADVENTURE_GAME),
        (PUZZLE_GAME, PUZZLE_GAME),
        (STRATEGY_GAME, STRATEGY_GAME),
        (SPORTS_GAME, SPORTS_GAME),
        (BOARD_AND_CARD_GAME, BOARD_AND_CARD_GAME),
        (OTHER_GAME, OTHER_GAME),
    )

    title = models.CharField(
        max_length=MAX_LEN_TITLE,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        choices=GAME_CHOICES,
        null=False,
        blank=False,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(MIN_RATING),
            MaxValueValidator(MAX_RATING),
        ),
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        validators=(
            MinValueValidator(MIN_VALUE_MAX_LEVEL),
        ),
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )
