from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm, UsernameField
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
	password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}))

	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'password')
		field_classes = {'username': UsernameField, 'email': forms.EmailField}

	def save(self, commit=True):
		user = super().save(commit=False)
		user.email = self.cleaned_data["email"]
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
			# if hasattr(self, "save_m2m"):
			# 	self.save_m2m()
		return user

class CustomUserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'is_active', 'is_staff')

class LoginForm(forms.Form):
	username_or_email = forms.CharField(label=_("Username/Email"))
	password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}))
