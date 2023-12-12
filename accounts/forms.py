from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Required. Include country code.')

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'password1', 'password2')
