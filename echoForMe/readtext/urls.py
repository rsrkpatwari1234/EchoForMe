from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('textToAudioNormalText/', views.textToAudioNormalText, name='textToAudioNormalText'),
    path('textToAudioNews/',views.texttoAudioNews, name='textToAudioNews'),
    path('NormalText/',views.normaltext, name='NormalText')
]