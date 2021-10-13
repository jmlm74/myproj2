"""
    app_utilisateurs URL Configuration

"""
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views

from app_utilisateurs import views as auv


app_name = 'app_utilisateurs'
urlpatterns = [
    path('list/', login_required(auv.UTilisateurListView.as_view()), name='list'),
]