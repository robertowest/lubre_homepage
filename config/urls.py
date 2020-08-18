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
from django.views.generic import TemplateView

from apps.accounts.views import LoginRedirect
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

    # redireccionamiento --------------------------------------------------------------
    path('redirect/', LoginRedirect, name='redirect'),

    # cartera -------------------------------------------------------------------------
    path('comunicacion/', include('apps.comunes.urls.comunicacion')),
    path('diccionario/', include('apps.comunes.urls.diccionario')),
    path('domicilio/', include('apps.comunes.urls.domicilio')),

    path('actividad/', include('apps.empresa.urls.actividad')),
    path('comercial/', include('apps.empresa.urls.comercial')),
    path('empresa/', include('apps.empresa.urls.empresa')),
    path('empresa_actividad/', include('apps.empresa.urls.empresa_actividad')),

    path('persona/', include('apps.persona.urls')),

    path('empleado/', TemplateView.as_view(template_name='default_base.html'), name='empleado'),
    path('gestion/', include('apps.firebird.urls')),


    path('prueba/', include('apps.prueba.urls')),
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
