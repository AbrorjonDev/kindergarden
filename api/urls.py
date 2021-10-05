from django.urls import path
from .views import *

urlpatterns = [
    # path('tuman/', TumanCV.as_view(), name="tuman-api"),
    # path('tuman/<int:pk>/', TumanUV.as_view(), name="tuman-update-api"),
    path('kg/', KGCV.as_view(), name="kindergarden-api"),
    path('kg/<int:pk>/', KGUV.as_view(), name="kindergarden-update-api"),
    path('tadbirlar/', TadbirCV.as_view(), name="tadbir-api"),
    path('tadbirlar/<int:pk>/', TadbirUV.as_view(), name="tadbir-update-api"),
    path('yangilik/', YangilikCV.as_view(), name="yangilik-api"),
    path('yangilik/<int:pk>/', YangilikUV.as_view(), name="yangilik-update-api"),
    path('rahbariyat/', RahbariyatCV.as_view(), name="rahbariyat-api"),
    path('rahbariyat/<int:pk>/', RahbariyatUV.as_view(), name="rahbariyat-update-api"),
    path('xodim/', XodimCV.as_view(), name="xodim-api"),
    path('xodim/<int:pk>/', XodimUV.as_view(), name="xodim-update-api"),
    path('post/',PostCV.as_view(), name="post-api"),
    path('post/<int:pk>/', PostUV.as_view(), name="post-update-api"),
    path('all-data/', AllDataView.as_view(), name="all-data"),
    path('kitchen/', KitchenCView.as_view(), name="oshxona-api"),
    path('kitchen/<int:pk>/', KitchenUView.as_view(), name="oshxona-update-api"),
    path('menu/', MenuView.as_view(), name="menu"),
    path('menu/<int:pk>/', MenuUV.as_view(), name="menu"),
    path('media-upload/',MediaCV.as_view(), name="media-upload-api"),
    path('media-upload/<int:pk>/', MediaUV.as_view(), name="media-upload-update-api"),
    path('menu-by-kg/<int:pk>/', MenuByKGView.as_view()),
    path('register/', RegisterView.as_view(), name="registration-api"),
    path('verify-email/', VerifyEmail.as_view(), name="verify-email-api"),
    path('password-reset/', CustomPasswordResetView.as_view(), name="password-reset-api"),

]