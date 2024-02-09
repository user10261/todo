from django.contrib.auth.models import AbstractUser
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    status = models.IntegerField(default=0, choices=(
        (0, 'In Progress'),
        (1, 'Completed'),
        (2, 'Deleted')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SignUp(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    telphone = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class AllLogin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.username




