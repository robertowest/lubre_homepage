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
    path('chaining/', include('smart_selects.urls')),   # django-smart-selects
    
    path('ejemplo/', TemplateView.as_view(template_name='default_base.html'), name='ejemplo'),


    # homepage-------------------------------------------------------------------------
    path('', include('apps.homepage.urls', namespace='homepage')),
    path('equivalencia/', include('apps.equivalencia.urls', namespace='equivalencia')),
    path('tienda/', include('apps.tienda.urls')),

    # inicio de sesión ----------------------------------------------------------------
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('apps.accounts.urls')),

    # redireccionamiento --------------------------------------------------------------
    path('redirect/', LoginRedirect, name='redirect'),

    # comunes -------------------------------------------------------------------------
    path('comunicacion/', include('apps.comunes.urls.comunicacion')),
    path('diccionario/', include('apps.comunes.urls.diccionario')),
    path('domicilio/', include('apps.comunes.urls.domicilio')),

    # cartera -------------------------------------------------------------------------
    path('empresas/empresa/', include('apps.empresa.urls.empresa')),
    path('empresas/actividad/', include('apps.empresa.urls.actividad')),
    path('empresas/comercial/', include('apps.empresa.urls.comercial')),
    path('empresas/empresa_actividad/', include('apps.empresa.urls.empresa_actividad')),

    # persona -------------------------------------------------------------------------
    path('persona/', include('apps.persona.urls')),

    # gestión d lubre -----------------------------------------------------------------
    path('gestion/', include('apps.firebird.urls')),

    # estación de servicios -----------------------------------------------------------
    path('media/estacion/eess_cafeteria.pdf', include('apps.eess.urlsPDF')),
    path('eess/', include('apps.eess.urls')),

    # recursos humanos ----------------------------------------------------------------
    path('rrhh/empleado/', include('apps.rrhh.urls.empleadoUrls')),
    path('rrhh/denuncia', include('apps.rrhh.urls.denunciaUrls')),
    path('rrhh/vacaciones/', include('apps.rrhh.urls.vacacionesUrls')),

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

        # ejemplos de interfáz gráfica
        path('ui/blank',                TemplateView.as_view(template_name='examples/blank.html'), name='blank'),
        path('ui/buttons',              TemplateView.as_view(template_name='examples/buttons.html'), name='buttons'),
        path('ui/cards',                TemplateView.as_view(template_name='examples/cards.html'), name='cards'),
        path('ui/charts',               TemplateView.as_view(template_name='examples/charts.html'), name='charts'),
        path('ui/forgot_password',      TemplateView.as_view(template_name='examples/forgot-password.html'), name='forgot_password'),
        path('ui/index',                TemplateView.as_view(template_name='examples/index.html'), name='index'),
        path('ui/login',                TemplateView.as_view(template_name='examples/login.html'), name='login'),
        path('ui/register',             TemplateView.as_view(template_name='examples/register.html'), name='register'),
        path('ui/tables',               TemplateView.as_view(template_name='examples/tables.html'), name='tables'),
        path('ui/utilities_animation',  TemplateView.as_view(template_name='examples/utilities-animation.html'), name='utilities_animation'),
        path('ui/utilities_border',     TemplateView.as_view(template_name='examples/utilities-border.html'), name='utilities_border'),
        path('ui/utilities_color',      TemplateView.as_view(template_name='examples/utilities-color.html'), name='utilities_color'),
        path('ui/utilities_other',      TemplateView.as_view(template_name='examples/utilities-other.html'), name='utilities_other'),
    ]

    # -----------------------------------------------------------------------------
    # DEBUG
    # -----------------------------------------------------------------------------
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
