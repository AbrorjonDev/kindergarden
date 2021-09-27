"""kg_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from api.views import VerifyEmailView
from api.views import PasswordResetConfirmAPIView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('dj-rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmAPIView.as_view(),
         name="password_reset_confirm"),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    re_path(
        r'^dj-rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email',
    ),    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),

    path('docs/', include_docs_urls(title='Training Center Api')),
    path('schemas/', get_schema_view(
        title="EWS Schema",
        description="API for all models",
        version="1.0.0"
      ), name="openapi-schema")
]
