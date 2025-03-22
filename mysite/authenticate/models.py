from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, password=None, **extra_fields):
    if not email:
      raise ValueError('Email field is required')
    if not first_name:
      raise ValueError('First name is required')
    if not last_name:
      raise ValueError('Last name is required')
    if not password:
      raise ValueError('Password is required')
    
    # Convert email to lowercase
    email = self.normalize_email(email)
    extra_fields.setdefault('first_name', first_name)
    extra_fields.setdefault('last_name', last_name)
    
    # Creates a new user
    user = self.model(email=email, **extra_fields)
    # Hashes the password
    user.set_password(password)
    # Saves the user to database
    user.save(using=self._db)
    return user
  
  def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self.create_user(email, first_name, last_name, password, **extra_fields)

class CustomUser(AbstractUser):
  username = None
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  # Assigns the CustomUserManager to CustomUser
  objects = CustomUserManager()

  def __str__(self):
    return self.email
  
class Income(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  source = models.CharField(max_length=150)
  date = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name} - {self.source}: ${self.amount}"
  
class Expense(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.CharField(max_length=150) 
  date = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name} - {self.category}: ${self.amount}"
  
class Budget(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  monthly_limit = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, default=0.00)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name} - Budget: ${self.monthly_limit}"


