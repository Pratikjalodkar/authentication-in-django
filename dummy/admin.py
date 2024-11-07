from django.contrib import admin
from .models import Interns
# Register your models here.
@admin.register(Interns)

class AdiminInterns(admin.ModelAdmin):
    list_display=('project_name','repo_link','branch')
    # list_display=('project_name','repo_link','branch',
    #              'task','task_assigned_by',
    #              'date','task_closure_time',
    #              'next_task','next_task_assigned_by')