from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class UserSignupForm(UserCreationForm):
  email = forms.EmailField(required=True)
  first_name = forms.CharField(max_length=30, required=True)
  last_name = forms.CharField(max_length=30, required=True)

  class Meta:
    model = CustomUser
    fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

  # Ensure email is unique
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if CustomUser.objects.filter(email=email).exists():
      raise forms.ValidationError('Email is already in use')
    return email

class UserLoginForm(AuthenticationForm):
  # Using email instead of username login
  username = forms.EmailField(label='Email', required=True)

