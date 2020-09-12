from django.urls import path

from . import views

app_name = 'PDF'

urlpatterns = [
    path('', views.PDFTemplateView.as_view()),
]
