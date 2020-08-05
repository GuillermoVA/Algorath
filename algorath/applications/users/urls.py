#
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        'users/', 
        views.UserListView.as_view(),
        name='user-list',
    ),
    path(
        'connections/', 
        views.ConnectionRegisterView.as_view(),
        name='connections',
    ),
    path(
        'user-connections/<pk>', 
        views.UserConnectionsListView.as_view(),
        name='user-connections',
    ),
]