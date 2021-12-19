"""
    app_utilisateurs URL Configuration

"""
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.contrib.auth import views as auth_views

from app_utilisateurs import views as auv


app_name = 'app_utilisateurs'
urlpatterns = [
    # path('list/', login_required(auv.UTilisateurListView.as_view()), name='list'),
    path('list/', login_required(auv.utilisateur_list_view), name='list'),
    path('display/<int:pk>', login_required(auv.UtilisateurDisplay.as_view()), name='display'),
    path('create/', login_required(auv.UtilisateurCreateView.as_view()), name='create_utilisateur'),
    path('delete/<int:pk>', login_required(auv.UtilisateurDeleteView.as_view()), name='delete'),
    path('update/<int:pk>', login_required(auv.UtilisateurUpdateView.as_view()), name='update'),
]
