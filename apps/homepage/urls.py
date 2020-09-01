from django.urls import path
from . import views

app_name = 'homepage'   # en template: request.resolver_match.app_name

urlpatterns = [
    # path('', views.index, name='homepage'),
    path('', views.IndexView.as_view(), name='homepage'),
    path('blog/', views.PostList.as_view(), name='post_list'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('categoria/<int:pk>/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('producto/<int:pk>/', views.ProductoDetail.as_view(), name='producto_detail'),
    path('service/<int:pk>/', views.ServiceDetail.as_view(), name='service_detail'),

    path('producto/busqueda/', views.BusquedaListView.as_view(), name='producto_search'),
]




from apps.comunes.views import mails
urlpatterns += [
    path('send_mail/', mails.test_send_mail),
    path('send_mail_template/', mails.test_send_mail_template),
    path('send_simple_mail/', mails.test_simple_mail),
]