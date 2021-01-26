from django.urls import path
from . import views

app_name = __package__.split('.')[1]

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.PersonaTemplateView.as_view(), name='index'),
]
