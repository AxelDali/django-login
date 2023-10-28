# login/urls.py

from django.urls import path, include

from .views import SignUpView

app_name = 'login'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]