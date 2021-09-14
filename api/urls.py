from django.urls import path
from .views import *

urlpatterns = [
    path('tuman/', TumanCV.as_view()),
    path('tuman/<int:pk>/', TumanUV.as_view()),
    path('kg/', KGCV.as_view()),
    path('kg/<int:pk>/', KGUV.as_view()),
    path('tadbirlar/', TadbirCV.as_view()),
    path('tadbirlar/<int:pk>/', TadbirUV.as_view()),
    path('yangilik/', YangilikCV.as_view()),
    path('yangilik/<int:pk>/', YangilikUV.as_view()),
    path('rahbariyat/', RahbariyatCV.as_view()),
    path('rahbariyat/<int:pk>/', RahbariyatUV.as_view())

]