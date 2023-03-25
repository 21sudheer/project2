from django import forms
from .models import Emp
from django.core.exceptions import ValidationError
from django.core import validators
#from django.contrib.auth.forms import UserCreationForm

def validate(value):
    if "gmail.com" in value:
        return value
    else:
        raise ValidationError("This field accepts mail id of google")
    
class Empform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirmpassword=forms.CharField(widget=forms.PasswordInput)

    email=forms.EmailField(max_length=200, validators=[validate])

    class Meta:
        model=Emp
        fields='__all__'
        #fields=['firstname','lastname','email','username']
        #exclude=['password','confirmpassword']

    def clean(self):
        cleaned_data=super().clean()
        firstname=cleaned_data.get('firstname')
        lastname=cleaned_data.get('lastname')
        username=cleaned_data.get('username') 

        if len(firstname) < 5:
            #raise ValidationError("minimum 5 characters required")
            self._errors['firstname'] = self.error_class(['Minimum 5 characters required'])
        if len(lastname) < 5:
            self._errors['lastname'] = self.error_class(['Minimum 5 characters required'])

        if len(username) < 5:
            self._errors['username'] = self.error_class(['Minimum 5 characters required'])

        return cleaned_data