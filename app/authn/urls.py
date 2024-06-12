from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('devteam/', views.devteam, name='devteam'),

    # path('login/', views.login_view, name='login'),
    # path('register/', views.register_view, name='register'),
]