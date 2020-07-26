from django.conf import settings
from django.conf.urls import handler400, handler403, handler404, handler500

if not settings.DEBUG:
    handler400 = 'apps.comunes.views.errores.bad_request'
    handler403 = 'apps.comunes.views.errores.permission_denied'
    handler404 = 'apps.comunes.views.errores.page_not_found'
    handler500 = 'apps.comunes.views.errores.server_error'
