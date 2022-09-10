from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control m-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control m-5'}),
        }
        labels = {
            'text': 'Write your thoughts here',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError('Only notes about django are allowed')
        if not title:
            raise ValidationError('Title cannot be empty')
        return title
