from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField("School Name", max_length=50)
    email_extension = models.CharField("Email Extension", max_length=50)

    @property
    def school_score(self):
        return_val = 0
        scores = self.students.all().values_list('score', flat=True)
        for i in scores:
            if not i == None :
                return_val += i
        return return_val

    def __str__(self):
        return self.name
    