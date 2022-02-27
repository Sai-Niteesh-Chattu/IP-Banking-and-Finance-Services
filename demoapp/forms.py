from django import forms
from .models import User,Student
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
