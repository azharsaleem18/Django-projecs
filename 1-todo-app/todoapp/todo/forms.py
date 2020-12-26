from django import forms
from django.forms import fields, widgets
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['name']
        labels = {'name' : 'Name'}
        widgets = {
            'name': forms.TextInput(attrs={'classes': 'form-control'})
        }

        def clean(self):
            fields = self.cleaned_data