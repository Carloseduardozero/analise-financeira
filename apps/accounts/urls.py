from django.urls import path
from django.contrib.auth.views import LoginView

from apps.accounts.views.auth_views import register_view

app_name = 'accounts'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='accounts/registration/login.html'),
        name='login',
    ),
    path('cadastro/', register_view, name='register'),
]
