from django.urls import path
from . import views

#app_name = 'authenticate'

urlpatterns = [
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('signup/', views.signup, name='signup'),

  path('dashboard/', views.dashboard, name='dashboard'),
  path('income/', views.income, name='income'),
  path('expense/', views.expense, name='expense'),
  path('budget/', views.budget, name='budget'),

  path('add-income/', views.add_income, name='add-income'),
  path('add-expense/', views.add_expense, name='add-expense'),
  path('set-budget/', views.add_budget, name='set-budget'),
  
  path('view-income/', views.view_income, name='view_income'),
  path('view-expense/', views.view_expense, name='view_expense'),
  path('view-budget/', views.view_budget, name='view_budget'),
]