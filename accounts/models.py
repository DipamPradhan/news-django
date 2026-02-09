from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(14), MaxValueValidator(90)],
    )
