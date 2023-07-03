from django import forms

from .models import Task

INPUT_CLASS = 'w-full py-4 px-6 rounded-lg border-2 border-indigo-900 bg-gray-200'

# some attributes are overriden here inorder to beautify the form


class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'due_date',)

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            }),
        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'due_date', 'is_completed')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            }),
        }

