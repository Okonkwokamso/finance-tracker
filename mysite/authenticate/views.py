from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserSignupForm, UserLoginForm
from .models import CustomUser

# Create your views here.
def signup(request):
  if request.method == 'POST':
    form = UserSignupForm(request.POST)
    if form.is_valid():
      user = CustomUser(
        email=form.cleaned_data['email'],
        first_name=form.cleaned_data['first_name'],
        last_name=form.cleaned_data['last_name']
      )

      # Hashes the password
      user.set_password(form.cleaned_data['password1'])
      user.save()
      messages.success(request, 'Account created successfully')
      # Logs user in
      login(request, user)
      return redirect('dashboard')
      # return redirect('dashboard') 
  else:
    form = UserSignupForm()
  
  return render(request, 'authenticate/signup.html', {'form': form})

def user_login(request):
  if request.method == 'POST':
    form = UserLoginForm(request, data=request.POST)
    if form.is_valid():
      email = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      
      try:
        user = CustomUser.objects.get(email=email)
      except CustomUser.DoesNotExist:
        user = None

      if user and user.check_password(password):
        login(request, user)
        return redirect('dashboard')  
      else: 
        form.add_error(None, 'Invalid email or password')
  else:
    form = UserLoginForm()

  return render(request, 'authenticate/login.html', {'form': form})

def user_logout(request):
  logout(request)
  return redirect('login')


def dashboard(request):
  html_content = "<h6>Welcome to the Dashboard</h6>"
  return HttpResponse(html_content)
