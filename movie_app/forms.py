from django.forms import ModelForm
from .models import Movie_data

class Movie_form(ModelForm):
    class Meta:
        model = Movie_data
        fields = '__all__'