from django.forms import ModelForm
from .models import UserCreation
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
   date_of_birth = forms.DateField(
         widget=forms.DateInput(attrs={'type': 'date'}),help_text = "Please enter your date of birth in YYYY-MM-DD format."
   )
   class Meta:
      model = UserCreation
      fields = ['first_name', 'last_name', 'username', 'email','gender', 'date_of_birth', 'country', 'phone_number', 'password1', 'password2']

