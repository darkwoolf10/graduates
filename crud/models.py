import os

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from graduates.settings import BASE_DIR


class Curator(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self):
        return self.name + " " + self.surname


class Diploma(models.Model):
    title = models.CharField(max_length=128)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Ball(models.Model):
    subject = models.CharField(max_length=64)
    assessment = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.subject


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
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32, null=True)
    photo = models.FilePathField(path=os.path.join(BASE_DIR) + '/static/assets/image', null=True)
    diploma = models.ForeignKey(Diploma, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ball = models.ForeignKey(Ball, on_delete=models.CASCADE)
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    curator = models.ForeignKey(Curator, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " " + self.surname
