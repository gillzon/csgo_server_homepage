from django.urls import path
from core.views.index import home, register, view_user
app_name = "core"

urlpatterns = [
    path('dashboard/', home, name="home"),
    path('register/', register, name="register"),
    path('player/<id>', view_user, name="player_details"),

]