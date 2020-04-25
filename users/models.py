from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """ Custome User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_FRENCH = "fr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_FRENCH, "French"),
    )

    CURRENCY_CFA = "cfa"
    CURRENCY_BTC = "btc"

    CURRENCY_CHOICES = ((CURRENCY_CFA, "CFA"), (CURRENCY_BTC, "BTC"))

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=3, blank=True)

    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=4, blank=True)

    superhost = models.BooleanField(default=False)
