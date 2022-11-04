from django.db import models

# Create your models here.

class Task(models.Model):
    label = models.CharField(max_length=100, blank=False, null=False)
    done = models.BooleanField(default=False, blank=True, null=True)
    
    class Meta:
        db_table= "tasks"