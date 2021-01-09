from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField

# Create your models here.
class CustomUser(AbstractUser):
    TOPICS_CHOICES = (
        ('Physics', 'Physics'),
        ('Pre-Calc', 'Pre-Calc')
    )

    INTEREST_CHOICES = (
        ('Football', 'Football'),
        ('Fencing', 'Fencing')
    )

    school = models.CharField(max_length=200)
    grade = models.IntegerField(blank=True, null=True)
    default_topics = MultiSelectField(choices=TOPICS_CHOICES)
    nickname = models.CharField(max_length=64)
    interest = MultiSelectField(choices=INTEREST_CHOICES)
    friends = models.ManyToManyField(
        'users.CustomUser'
    )
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.email