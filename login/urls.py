# login/urls.py

from django.urls import path, include, reverse_lazy

from .views import SignUpView
from django.contrib.auth import views as auth_views

app_name = 'login'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name= 'registration/password_reset_form.html',
            email_template_name= 'registration/password_reset_email.html',
            success_url= reverse_lazy('login:password_reset_done')
        ),
        name= 'password_reset'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url= reverse_lazy('login:password_reset_complete')
        ),
        name= 'password_reset_confirm'
    ),
    path('', include('django.contrib.auth.urls')),
]