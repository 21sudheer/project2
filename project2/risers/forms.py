from django import forms
from .models import Emp
#from django.contrib.auth.forms import UserCreationForm

class Empform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirmpassword=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Emp
        fields=['firstname','lastname','email','username']
        exclude=['password','confirmpassword']