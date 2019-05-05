import os

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from graduates.settings import TODAY


class Curator(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to='static/assets/image', default='static/assets/image/default.png', blank=True)

    def __str__(self):
        return self.name + " " + self.surname


class Diploma(models.Model):
    title = models.CharField(max_length=128)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE, related_name='curator')

    def __str__(self):
        return self.title


class Ball(models.Model):
    physical = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(60)
        ],
        default='60'
    )
    programing = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(60)
        ],
        default='60'
    )
    math = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(60)
        ],
        default='60'
    )


class Work(models.Model):
    title = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.title


class Faculty(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=32)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='group', default='1')
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32, null=True)
    photo = models.ImageField(upload_to='static/assets/image', default='static/assets/image/default.png', blank=True)
    diploma = models.ForeignKey(Diploma, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ball = models.ForeignKey(Ball, on_delete=models.CASCADE, related_name='ball', null=True, blank=True)
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name='work', null=True, blank=True)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    year_end = models.IntegerField(default=TODAY.year)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name + " " + self.surname
