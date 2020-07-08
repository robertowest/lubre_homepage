"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),

    # homepage-------------------------------------------------------------------------
    path('', include('apps.homepage.urls', namespace='homepage')),
    path('equivalencia/', include('apps.equivalencia.urls', namespace='equivalencia')),
    path('tienda/', include('apps.tienda.urls')),

    # inicio de sesión ----------------------------------------------------------------
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),

    # cartera -------------------------------------------------------------------------
    path('comunicacion/', include('apps.comunes.urls.comunicacion')),
    path('diccionario/', include('apps.comunes.urls.diccionario')),
    path('domicilio/', include('apps.comunes.urls.domicilio')),

    path('empresa/', include('apps.empresa.urls.empresa')),
    path('empresa/actividad/', include('apps.empresa.urls.actividad')),

    path('persona/', include('apps.persona.urls')),
] 

# Dashboard
from django.views.generic import TemplateView
urlpatterns += [
    # path('', TemplateView.as_view(template_name='dashboard.html'))
    # path('cartera/', TemplateView.as_view(template_name='cartera_base.html'), name='cartera')
    path('cartera/', TemplateView.as_view(template_name='dashboard.html'), name='cartera')
]

# -----------------------------------------------------------------------------
# DEBUG
# -----------------------------------------------------------------------------
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
