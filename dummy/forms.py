from django import forms
from .models import Interns
from django.core.exceptions import ValidationError

class InternsForm(forms.ModelForm):
    class Meta:
        model = Interns
        fields = ['project_name','repo_link','branch']
        # fields = ['project_name','repo_link','branch',
        #          'task','task_assigned_by',
        #          'date','task_closure_time',
        #          'next_task','next_task_assigned_by']


        #validation
        def clean_project_name(self):
            cleaned_data = super().clean()
            project_name = cleaned_data.get('project_name')
            
            if len(project_name):
                raise ValidationError('atleast 4 character long')
            
            return project_name
            

        