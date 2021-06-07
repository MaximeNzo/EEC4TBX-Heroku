from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('logout', views.logout),
    path('test', views.test),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
