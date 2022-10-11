from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):

    taskname = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status=  models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.taskname