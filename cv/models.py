from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')


