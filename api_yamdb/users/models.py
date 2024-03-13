from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models

from django.core.validators import RegexValidator
from django.core.validators import MaxLengthValidator
from django.utils.translation import gettext_lazy as _

LEN = 150


class User(AbstractUser):
    class Status(models.TextChoices):
        ANON = 'AN', _('anonymous')
        USER = 'US', _('user')
        MODERATOR = 'MD', _('moderator')
        ADMIN = 'AD', _('admin'),
        SUPERUSER = 'SU', _('superuser'),

    username = models.CharField(
        max_length=LEN,
        # validators=[
        #     RegexValidator(
        #         regex=r'^[\w.@+-]+\Z',
        #         message='this invalid name',
        #         code='invalid registration',
        #     ),
        #     MaxLengthValidator(LEN)

        # ],
        unique=True,
    )
    email = models.EmailField(
        max_length=254,
        unique=True,
        # validators=[
        #     MaxLengthValidator(LEN)
        # ]
        )
    role = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.USER,
    )
    first_name = models.CharField(
        max_length=LEN,
    )
    last_name = models.CharField(
        max_length=LEN,
        # validators=[MaxLengthValidator(LEN)]
    )
    bio = models.TextField()
