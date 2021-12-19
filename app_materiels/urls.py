"""
    app_materiels URL Configuration

"""
from django.contrib.auth.decorators import login_required
from django.urls import path

from app_materiels import views as amv


app_name = 'app_materiels'
urlpatterns = [
    # path('list/', login_required(auv.UTilisateurListView.as_view()), name='list'),
    # path('list/', login_required(auv.utilisateur_list_view), name='list'),
]