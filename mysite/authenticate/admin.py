from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Income, Expense, Budget

class CustomUserAdmin(UserAdmin):
  model = CustomUser
  list_display = ("email", "first_name", "last_name", "has_income", "has_expense", "has_budget", "is_staff", "is_active")
  search_fields = ("email", "first_name", "last_name")
  ordering = ("email",)

  fieldsets = (
    (None, {"fields": ("email", "password")}),
    ("Personal Info", {"fields": ("first_name", "last_name")}),
    ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    ("Important Dates", {"fields": ("last_login", "date_joined")}),
  )

  add_fieldsets = (
    (None, {
      "classes": ("wide",),
      "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
    }),
  )

  def has_income(self, obj):
    return Income.objects.filter(user=obj).exists()
  has_income.boolean = True
  has_income.short_description = 'Income'

  def has_expense(self, obj):
    return Expense.objects.filter(user=obj).exists()
  has_expense.boolean = True
  has_expense.short_description = 'Expense'

  def has_budget(self, obj):
    return Budget.objects.filter(user=obj).exists()
  has_budget.boolean = True
  has_budget.short_description = 'Budget'

admin.site.register(CustomUser, CustomUserAdmin)
