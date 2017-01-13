from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^regions/', views.highscores, name='regions')
]