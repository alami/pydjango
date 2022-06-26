from django.db import models

# Create your models here.
from django.db.models import TextChoices


class Country(TextChoices):
    ENGLAND = "ENG", "Англия"
    RUSSIA = "RU", "Россия"
    ESP = "ESP", "Испания"


class Team(models.Model):
    name = models.TextField()
    country = models.TextField()
    city = models.TextField()