from django.db import models
from django.forms import ModelForm


class Tasks(models.Model):
    Task_Name = models.CharField(max_length=64)
    Task_Description = models.CharField(max_length=256)
    Task_Type = models.CharField(
        max_length=256,
        choices=[
            ('MJ',"Major"),
            ('MN',"Minor"),
            ('PRJ',"Project")
        ]
    )
    Task_Grade = models.DecimalField(max_digits=5, decimal_places=2)
    Due_Date = models.DateTimeField()

class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['Task_Name', 'Task_Description', 'Task_Type', 'Task_Grade', 'Due_Date']