from django.db import models


# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')


class Education(models.Model):
    university = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('SkillCategory', on_delete=models.DO_NOTHING, null=True)
    level = models.IntegerField('level of skill range from 0 to 10', blank=True, null=True)

    def display_category(self):
        return self.category.name


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=9)
