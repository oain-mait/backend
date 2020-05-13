from django.db import models

# Create your models here.


class FinalProjectModel(models.Model):
    name = models.CharField(max_length=64)
    course_1 = models.CharField(max_length=128)
    course_2 = models.CharField(max_length=128)
