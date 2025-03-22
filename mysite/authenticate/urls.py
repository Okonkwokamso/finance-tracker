from django.urls import path
from . import views

#app_name = 'authenticate'

urlpatterns = [
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('signup/', views.signup, name='signup'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('add-income/', views.add_income, name='income'),
  path('add-expense/', views.add_expense, name='expense'),
  path('set-budget/', views.add_budget, name='budget'),
]










