from django.db import models
from django.contrib.auth.models import User# Create your models here.
from datetime import date 
from datetime import datetime


class TodoTable(models.Model):
    task_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    task_name = models.CharField(max_length = 100)
    task_disc = models.CharField(max_length = 200)
    task_time = models.TimeField(default = datetime.now().time().strftime('%H:%M:%S'))
    task_date = models.DateField(default = date.today().strftime('%Y-%m-%d'))
    task_status = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
    
    