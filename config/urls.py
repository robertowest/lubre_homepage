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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
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

    # estación de servicios -----------------------------------------------------------
    path('media/estacion/eess_cafeteria.pdf', include('apps.eess.urlsPDF')),
    path('eess/', include('apps.eess.urls')),

    # recursos humanos ----------------------------------------------------------------
    path('rrhh/', include('apps.rrhh.urls')),

    # afip ---------------------------------------------------------------------------
    path('afip/', include('apps.afip_test.urls')),

    # MP -----------------------------------------------------------------------------
    path('mercadopago/', include('django_mercadopago.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # -----------------------------------------------------------------------------
    # Esto permite que las páginas de error se depuren durante el desarrollo
    # simplemente visite estas URL para ver cómo se ven estas páginas de error.
    # -----------------------------------------------------------------------------
    urlpatterns += [
        path("400/", default_views.bad_request, kwargs={"exception": Exception("Solicitud incorrecta!")},),
        path("403/", default_views.permission_denied, kwargs={"exception": Exception("Permiso denegado")},),
        path("404/", default_views.page_not_found, kwargs={"exception": Exception("Página no encontrada")},),
        path("500/", default_views.server_error),
    ]


    # -----------------------------------------------------------------------------
    # DEBUG
    # -----------------------------------------------------------------------------
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
