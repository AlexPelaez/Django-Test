from django.conf.urls import url

from django.urls import path, re_path

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
urlpatterns = [
    
    path('login/', LoginView.as_view(template_name='accounts/login_register.html'), name="login_view"),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    url(r'register/$', views.register, name='register'),
    url(r'profile$', views.view_profile, name='view_profile'),
    url(r'profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', PasswordResetView.as_view (from_email='reset_password')),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view (template_name='reset_password_done')),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view (template_name='reset_password_complete')),
]
