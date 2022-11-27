from django.urls import path
from core.views.index import home, register, player_detailed_view

app_name = "core"

urlpatterns = [
    path('dashboard/', home, name="home"),
    path('register/', register, name="register"),
    path('player/<id>', player_detailed_view, name="player_details"),
]
