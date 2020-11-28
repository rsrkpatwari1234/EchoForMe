from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('textToAudio/', views.textToAudio, name='textToAudio'),
    path('textToAudioNews/',views.texttoAudioNews, name='textToAudioNews')
]