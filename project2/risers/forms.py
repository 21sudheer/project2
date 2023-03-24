from django import forms
from .models import Emp
from django.core.exceptions import ValidationError
from django.core import validators
#from django.contrib.auth.forms import UserCreationForm

class Empform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirmpassword=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Emp
        fields=['firstname','lastname','email','username']
        exclude=['password','confirmpassword']

    def clean(self):
        cleaned_data=super().clean()
        firstname=cleaned_data.get('firstname')
        lastname=cleaned_data.get('lastname')     
        if len('firstname') < 5:
            raise ValidationError("minimum 5 characters required")    
        if len('lastname') < 5:
            print("minimum 5 characters required")