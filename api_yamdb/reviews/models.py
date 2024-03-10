from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.PositiveSmallIntegerField()
    category = models.ForeignKey(
        to=Category,
        on_delete=models.PROTECT,
    )

class Review(models.Model):
    title = models.ForeignKey(
        to=Title,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT
    )
    score = models.PositiveSmallIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    review = models.ForeignKey(
        to=Review,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.PROTECT,
    )
    pub_date = models.DateTimeField(auto_now_add=True)



class GenreTitle(models.Model):
    title = models.ForeignKey(
        to=Title,
        on_delete=models.PROTECT,
    )
    genre = models.ForeignKey(
        to=Genre,
        on_delete=models.PROTECT
    )