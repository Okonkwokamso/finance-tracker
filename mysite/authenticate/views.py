from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.db import models
from .forms import UserSignupForm, UserLoginForm, IncomeForm, ExpenseForm, BudgetForm
from .models import CustomUser, Budget, Income, Expense

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
  return render(request, 'authenticate/dashboard.html')

@login_required
def income(request):
  return render(request, 'authenticate/income.html')

@login_required
def expense(request):
  return render(request, 'authenticate/expense.html')

@login_required
def budget(request):
  return render(request, 'authenticate/budget.html')

@login_required
def view_income(request):
  incomes = Income.objects.filter(user=request.user).order_by('-date')
  return render(request, 'authenticate/view_income.html', {'incomes': incomes})

@login_required
def view_expense(request):
  expenses = Expense.objects.filter(user=request.user).order_by('-date')
  return render(request, 'authenticate/view_expense.html', {'expenses': expenses})

@login_required
def view_budget(request):
  budget = Budget.objects.filter(user=request.user).first()
  return render(request, 'authenticate/view_budget.html', {'budget': budget})
  

@login_required
def add_income(request):
  if request.method == 'POST':
    form = IncomeForm(request.POST)
    if form.is_valid():
      income = form.save(commit=False)
      income.user = request.user
      print(type(request.user))
      income.save()
      messages.success(request, 'Income added successfully')
      return redirect('dashboard')
  else:
    form = IncomeForm()
  return render(request, 'authenticate/add_income.html', {'form': form})

@login_required
def add_expense(request):
  if request.method == 'POST':
    form = ExpenseForm(request.POST)
    if form.is_valid():
      expense = form.save(commit=False)
      expense.user = request.user
      expense.date = now().date()
      expense.save()

      # Calculate total expenses for the current month
      current_month_expense = Expense.objects.filter(
        user=request.user, 
        date__month=now().month,
        date__year=now().year
      ).aggregate(total=models.Sum('amount'))['total'] or 0

      # Get the budget for the current month
      budget = Budget.objects.filter(user=request.user).first()

      if budget and current_month_expense > budget.monthly_limit:
        warning_message = f"Your total monthly expenses ${current_month_expense} has exceeded your budget ${budget.monthly_limit}"
        
        messages.warning(request, warning_message)

      messages.success(request, 'Expense added successfully')
      return redirect('dashboard')
  else:
    form = ExpenseForm()
  return render(request, 'authenticate/add_expense.html', {'form': form})

@login_required
def add_budget(request):
  if request.method == 'POST':
    form = BudgetForm(request.POST)
    if form.is_valid():
      print('Form is valid')
      print('Cleaned Data:', form.cleaned_data)

      budget, created = Budget.objects.get_or_create(user=request.user)
      budget.monthly_limit = form.cleaned_data['monthly_limit']
      budget.save()
      messages.success(request, 'Budget added successfully')
      return redirect('dashboard')

      
  else:
    form = BudgetForm()
  return render(request, 'authenticate/set_budget.html', {'form': form})
