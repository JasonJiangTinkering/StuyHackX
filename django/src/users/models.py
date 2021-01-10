from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField
from school.models import School

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

    school = models.ForeignKey(School, verbose_name='school', related_name='students', on_delete=models.CASCADE, null=True, blank=True)

    grade = models.IntegerField(blank=True, null=True)
    default_topics = MultiSelectField(choices=TOPICS_CHOICES, blank=True, null=True)
    nickname = models.CharField(max_length=64)
    interest = MultiSelectField(choices=INTEREST_CHOICES, blank=True, null=True)
    friends = models.ManyToManyField(
        'users.CustomUser',
        blank=True,
    )
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.school is None:
            email_extension = self.email.split('@')[1]
            school = School.objects.filter(email_extension=email_extension)
            
            if school.count() > 0:
                self.school = school[0]

            super().save(*args, **kwargs)