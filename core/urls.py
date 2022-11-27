from django.urls import path
from core.views.index import (
    home,
    register,
    player_detailed_view,
    server_info, 
    user_profile
)

app_name = "core"

urlpatterns = [
    path('dashboard/', home, name="home"),
    path('server_info/', server_info, name="server_info"),
    path('register/', register, name="register"),
    path('player/<id>', player_detailed_view, name="player_details"),
    path('user_profile/', user_profile, name="user_profile"),
]
