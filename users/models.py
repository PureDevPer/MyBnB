from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_CHINESE = "chinese"
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_FRENCH = "french"
    LANGUAGE_GERMAN = "german"
    LANGUAGE_HINDI = "hindi"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_SPANISH = "spanish"

    LANGUAGE_CHOICES = (
        (LANGUAGE_CHINESE, "Chinese"),
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_FRENCH, "French"),
        (LANGUAGE_GERMAN, "German"),
        (LANGUAGE_HINDI, "Hindi"),
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_SPANISH, "Spanish"),
    )

    CURRENCY_EUR = "eur"
    CURRENCY_KRW = "krw"
    CURRENCY_USD = "usd"
    CURRENCY_YUAN = "yuan"

    CURRENCY_CHOICES = (
        (CURRENCY_EUR, "EURO"),
        (CURRENCY_KRW, "KRW"),
        (CURRENCY_USD, "USD"),
        (CURRENCY_YUAN, "YUAN"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, blank=True)
    superhost = models.BooleanField(default=False)
