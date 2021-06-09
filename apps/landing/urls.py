from django.urls import path
from . import views

app_name = 'landing'   # en template: request.resolver_match.app_name

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]