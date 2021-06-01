from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    # Meta class keeps configuration in one place.
    class Meta:
        model = User
        # Fields I want in my form in order I want it.
        fields = ['username', 'email', 'password1', 'password2']
