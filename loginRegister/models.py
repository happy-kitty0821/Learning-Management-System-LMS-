from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
# class Users(AbstractUser):
#     ACCOUNT_TYPE_CHOICES = [
#         ('student', 'Student'),
#         ('teacher', 'Teacher')
#     ]
#     accountType = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='student')

#     def __str__(self):
#         return self.username

