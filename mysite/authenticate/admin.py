from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
  list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
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

admin.site.register(CustomUser, CustomUserAdmin)
