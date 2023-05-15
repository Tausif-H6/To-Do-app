from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null= True,blank = True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    reminder_date = models.DateField(null=True, blank=True, attrs={'placeholder': 'Select a date'})
    reminder_time = models.TimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['complete']