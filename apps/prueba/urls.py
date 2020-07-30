from django.urls import path

from . import views

app_name = __package__.split('.')[1]

urlpatterns = [
    path('<int:pk>/', views.PruebaDetailView.as_view(), name='detail'),
    path('search/', views.SearchDataView.as_view(), name='search_data'),
    path('comercial1/', views.comercial1, name='comercial1'),
    path('comercial2/', views.comercial2.as_view(), name='comercial2'),
    path('comercial3/', views.comercial3, name='comercial3'),
]
