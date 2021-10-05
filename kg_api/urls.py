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
from django.urls import path, include, re_path, reverse
from api.views import VerifyEmailView
from api.views import PasswordResetConfirmAPIView
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django.conf import settings
from django.conf.urls.static import static

@api_view(['GET'])
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response({
        "rahbariyat": "https://bogcha.herokuapp.com/rahbariyat/",
        "kindergarden": "https://bogcha.herokuapp.com/kg/",
        "tadbirlar": "https://bogcha.herokuapp.com/tadbirlar/",
        "yangilik": "https://bogcha.herokuapp.com/yangilik/",
        "xodim": "https://bogcha.herokuapp.com/xodim/",
        "post": "https://bogcha.herokuapp.com/post/",
        "kitchen": "https://bogcha.herokuapp.com/kitchen/",
        "menu": "https://bogcha.herokuapp.com/menu/",
        "all-data": "https://bogcha.herokuapp.com/all-data/",
        "media-upload": "https://bogcha.herokuapp.com/media-upload/",
    })
urlpatterns = [
    path('', api_root, name="api-root"),
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
    # path('rest-auth/', include('rest_auth.urls')),
    path('docs/', include_docs_urls(title='Bog\'cha Api')),
    path('schemas/', get_schema_view(
        title="EWS Schema",
        description="API for all models",
        version="1.0.0"
      ), name="openapi-schema")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)