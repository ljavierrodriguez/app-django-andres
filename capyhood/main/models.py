from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class Task(models.Model):
    label = models.CharField(max_length=100, blank=False, null=False)
    done = models.BooleanField(default=False, blank=True, null=True)
    start = models.DateTimeField(default=datetime.now, blank=False, null=False)
    end = models.DateTimeField(default=(datetime.now()+timedelta(weeks=2)), blank=True, null=True)
    
    class Meta:
        db_table= "tasks"