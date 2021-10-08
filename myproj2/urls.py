
from django.contrib import admin
from django.urls import path,include
import debug_toolbar

from app_user import views as apuv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', apuv.home, name='home'),
    path('signup/', apuv.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('app_user/', include('app_user.urls')),
]


