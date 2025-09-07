
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Включить URL-адреса аутентификации по умолчанию.
    path('', include('django.contrib.auth.urls')),
    # Страница выхода из системы.
    path('logged_out/', views.logout_view, name='logged_out'),
    # Страница регистрации.
    path('register/', views.register, name='register'),
]
