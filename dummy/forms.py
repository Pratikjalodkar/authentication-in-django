from django import forms
from .models import Interns
from django.core.exceptions import ValidationError
from django.core import validators

class InternsForm(forms.ModelForm):
    class Meta:
        model = Interns
        fields = ['project_name','repo_link','branch','task','task_assigned_by']
        
        
        # fields = ['project_name','repo_link','branch',
        #          'task','task_assigned_by',
        #          'date','task_closure_time',
        #          'next_task','next_task_assigned_by']


        #validation
    def clean_project_name(self):
        project_name = self.cleaned_data.get('project_name')
        
        if project_name=='':
            raise ValidationError('Enter Project Name')
        elif len(project_name)<3:
            raise ValidationError('project name must be atleast 3 character long')
        
        return project_name
    
    def clean_branch(self):
        branch = self.cleaned_data.get('branch')
        
        if branch == '':
            raise ValidationError('Please Enter branch name')
        
        return branch
            

        