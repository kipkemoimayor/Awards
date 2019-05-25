from .models import Projects,Rates
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model=Projects
        exclude=['user','design','usability','content']

class RateForm(forms.ModelForm):
    class Meta:
        model=Rates
        exclude=['user','project']
