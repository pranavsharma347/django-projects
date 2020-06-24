from django import forms
from myapp.models import Student
from django.contrib.auth.models import User

class Insert(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class Signup(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

