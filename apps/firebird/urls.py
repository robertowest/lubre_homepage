from django.urls import path

from . import views

app_name = 'gestion'

urlpatterns = [
     path('dashboard', views.dashboard, name='dashboard'),
]
