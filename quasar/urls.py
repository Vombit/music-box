from django.contrib import admin
from django.urls import path, include

from music_player import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    # path('', include('music_player.urls')),
]
