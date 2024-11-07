from django import forms
from .models import Interns

class InternsForm(forms.ModelForm):
    class Meta:
        model = Interns
        fields = ['project_name','repo_link','branch']
        # fields = ['project_name','repo_link','branch',
        #          'task','task_assigned_by',
        #          'date','task_closure_time',
        #          'next_task','next_task_assigned_by']
        