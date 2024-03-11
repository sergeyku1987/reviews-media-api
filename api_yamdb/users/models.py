from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import validate_name


class User(AbstractUser):
    class Status(models.TextChoices):
        ANON = 'AN', 'Anonymous'
        USER = 'US', 'User'
        MODERATOR = 'MD', 'Moderator'
        ADMIN = 'AD', 'Admin'
        SUPERUSER = 'SU', 'Superuser'

    username = models.CharField(
        max_length=150,
        validators=[validate_name],
        unique=True,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.USER,
    )
