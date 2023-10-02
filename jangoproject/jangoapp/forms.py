from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
    labels = {
      'student_number': 'Student Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'field_of_study': 'Field of Study',
      'gpa': 'GPA'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
    }


class UserForm(UserCreationForm):
  email = forms.EmailField(required=True)
  def __init__(self, *args, **kwargs):
    super(UserForm, self).__init__(*args, **kwargs)

    for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
  class Meta:
    model = User
    fields = ('username','email','password1')