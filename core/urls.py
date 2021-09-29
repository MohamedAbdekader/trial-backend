from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('users/', include('profiles.urls')),
    path('listings/', include('listings.urls')),
    path('comments/', include('comments.urls')),
]
