# myapp/forms.py
from django import forms

class TriageForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    transcript = forms.CharField(label='Message', widget=forms.Textarea)
