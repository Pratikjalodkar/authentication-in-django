from django.db import models
from django.contrib.auth.models import User
from django.core import validators

class Interns(models.Model):
    project_name = models.CharField(max_length=50, primary_key=True)
    repo_link = models.URLField(max_length=50)
    branch = models.CharField(max_length=50)
    # task = models.CharField(max_length=50)
    # task_assigned_by = models.CharField(max_length=50)
    # date = models.DateField()
    # task_closure_time = models.TimeField()
    # next_task = models.CharField(max_length=50)
    # next_task_assigned_by = models.CharField(max_length=50)

    def __str__(self):
        return self.project_name
