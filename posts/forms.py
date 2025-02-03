from django import forms
from .models import Soln

class SolnForm(forms.ModelForm):
    class Meta:
        model = Soln
        fields = ['title', 'link', 'explaination', 'code']
