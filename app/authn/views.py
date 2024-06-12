from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import CustomUserCreationForm, LoginForm
from .models import CustomUser

# Create your views here.

def devteam(request):
	return render(request, 'devteam.html')

@ensure_csrf_cookie
def index(request):
	if request.method == 'POST':
		if 'login' in request.POST:
			email = request.POST.get('username')
			password = request.POST.get('password')
			try:
				# Try to find the user by username first
				user = CustomUser.objects.get(username=email)
			except CustomUser.DoesNotExist:
				# If not found by username, try to find by email
				try:
					user = CustomUser.objects.get(email=email)
				except CustomUser.DoesNotExist:
					user = None

			if user is not None and user.check_password(password):
				# auth_login(request, user)
				return HttpResponse("User authenticated.")
			else:
				# Handle invalid login here
				return HttpResponse("Failed to login.")

		elif 'register' in request.POST:
			username = request.POST.get('username')
			email = request.POST.get('email')
			password = request.POST.get('password')
			try:
				user = CustomUser.objects.create_user(username=username, email=email, password=password)
				user.save()
				# Log the user in after registration
				# auth_login(request, user)
				return HttpResponse("User created.")
			except Exception as e:
				# Handle registration error (e.g., user already exists)
				return HttpResponse("Failed to register.")

	return render(request, 'index.html')
