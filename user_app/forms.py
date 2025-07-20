from django.forms import ModelForm
from .models import UserCreation
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
   class Meta:
      model = UserCreation
      fields = ['first_name', 'last_name', 'username', 'email','gender', 'date_of_birth', 'country', 'phone_number', 'password1', 'password2']

