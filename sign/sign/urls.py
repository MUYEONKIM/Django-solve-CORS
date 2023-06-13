"""
URL configuration for sign project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.utils.translation import gettext_lazy as _
from rest_auth.registration.views import VerifyEmailView, RegisterView
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from sign.views import ConfirmEmailView

from rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # allauth
    path('accounts/', include('allauth.urls')),

    # 로그인
    path('rest-auth/login', LoginView.as_view(), name='rest_login'),
    path('rest-auth/logout', LogoutView.as_view(), name='rest_logout'),
    path('rest-auth/password/change', PasswordChangeView.as_view(), name='rest_password_change'),
    path('rest-auth/', include('rest_auth.urls'), name='rest_auth'),

    # 회원가입
    path('rest-auth/registration', include('rest_auth.registration.urls'), name='rest_register'),
    path('login/success/', LoginView.as_view(), name='rest_login_success'),
    # 이메일 관련 필요
    path('accounts/allauth/', include('allauth.urls')),
    # 유효한 이메일이 유저에게 전달
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    # 유저가 클릭한 이메일(=링크) 확인
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
]
