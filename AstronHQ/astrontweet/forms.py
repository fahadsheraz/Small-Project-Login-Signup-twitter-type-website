from django import forms
from .models import astrontweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class astrontweetform(forms.ModelForm):
    class Meta:
        model = astrontweet
        fields = ['text', 'photo']
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')