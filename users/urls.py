
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    # Включить URL-адреса аутентификации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница выхода из системы.
    path('logged_out/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logged_out'),
    # Страница регистрации.
    path('register/', views.register, name='register'),
]
