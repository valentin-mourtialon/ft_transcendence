from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	add_form_template = "admin/auth/user/add_form.html" # FIXME
	change_user_password_template = None
	form = CustomUserChangeForm
	add_form = CustomUserCreationForm
	change_password_form = AdminPasswordChangeForm

	fieldsets = (
		(None, {"fields": ("username", "password")}),
		(_("Personal info"), {"fields": ("email",)}),
		(
			_("Permissions"),
			{
				"fields": (
					"is_active",
					"is_staff",
					"is_superuser",
					"groups",
					"user_permissions",
				),
			},
		),
		(_("Important dates"), {"fields": ("last_login", "date_joined")}),
	)
	add_fieldsets = (
		(
			None,
			{
				"classes": ("wide",),
				"fields": ("username", "email", "password"),
			},
		),
	)
	list_display = ("username", "email", "is_staff")
	list_filter = ("is_staff", "is_superuser", "is_active", "groups")
	search_fields = ("username", "email")
	ordering = ("username",)
	filter_horizontal = (
		"groups",
		"user_permissions",
	)

	def get_fieldsets(self, request, obj=None):
		if not obj:
			return self.add_fieldsets
		return super().get_fieldsets(request, obj)

	# TODO
