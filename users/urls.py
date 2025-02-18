from django.contrib.auth import views as auth_views
from django.urls import path
from .views import RegisterView, logout

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', logout, name='logout'),
]