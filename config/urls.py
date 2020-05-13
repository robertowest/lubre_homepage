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

    # homepage y equivalencias (juntos)
    path('', include('apps.homepage.urls', namespace='homepage')),
    path('equivalencia/', include('apps.equivalencia.urls', namespace='equivalencia')),

    # inicio de sesión
    path('accounts/', include('apps.accounts.urls')),
    path('tienda/', include('apps.tienda.urls')),
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
