from django.urls import path, include
from . import views
app_name = 'app_user'

urlpatterns = [
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
]
