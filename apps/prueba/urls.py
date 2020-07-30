from django.urls import path
from . import views

app_name = __package__.split('.')[1]

urlpatterns = [
    path('<int:pk>/', views.PruebaDetailView.as_view(), name='detail'),
]
