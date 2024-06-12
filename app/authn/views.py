from django.contrib.auth import authenticate, login
from django.shortcuts import render
from .forms import CustomUserCreationForm, LoginForm

# Create your views here.

def index(request):
	form_login = LoginForm()
	form_register = CustomUserCreationForm()
	if request.method == 'POST':
		if 'login' in request.POST:
			form_login = LoginForm(request.POST)
			if form_login.is_valid():
				username_or_email = form_login.cleaned_data['username_or_email']
				password = form_login.cleaned_data['password']
				user = authenticate(request, username=username_or_email, password=password)
				if user is not None:
					login(request, user)
					return redirect('home')  # Redirect to home or any other page after login
				else:
					form_login.add_error(None, 'Invalid username or password')
		elif 'register' in request.POST:
			form_register = CustomUserCreationForm(request.POST)
			if form_register.is_valid():
				form_register.save()
				return redirect('login')  # Redirect to login page after registration
			else:
				form_register.add_error(None, 'Invalid username or password')

	context = {
		'form_login': form_login,
		'form_register': form_register,
	}

	return render(request, 'index.html', context)
