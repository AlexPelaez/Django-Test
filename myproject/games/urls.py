from django.conf.urls import url

from django.urls import path, re_path

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
urlpatterns = [
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view (template_name='reset_password_complete')),
]
