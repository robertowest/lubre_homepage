from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, reverse, render

# How to use
# obj = [User].objects.create()
# get_app_name(obj)
# get_model_name(obj)

# __package__.split('.')[1]
# self._meta.verbose_name.lower()

def get_app_name(model):
    obj_content_type = ContentType.objects.get_for_model(model)
    return obj_content_type.app_label


def get_model_name(model):
    obj_content_type = ContentType.objects.get_for_model(model)
    return obj_content_type.model


def redirect_to(request, reverse_url, type="GET"):
    # si existe la directiva "next", redirecciona la salida hacia allí
    # si no existe utilizará "reverse_url"
    if (type == "GET"):
        redirect_to = request.GET.get('next')
    else:
        redirect_to = request.POST.get('next')

    if not redirect_to:
        redirect_to = reverse_url
    return redirect(redirect_to)


def redirect_to_with_next(request, reverse_url, type="GET"):
    # si existe la directiva "next", la recupera pa volver a pasarla como parámetro a "reverse_url"
    if (type == "GET"):
        redirect_to = request.GET.get('next')
    else:
        redirect_to = request.POST.get('next')

    if redirect_to:
        redirect_to = reverse(reverse_url) + "?next=" + redirect_to
    else:
        redirect_to = reverse(reverse_url)

    return redirect(redirect_to)


def get_url_referer(request, reverse_url):
    remove = request._current_scheme_host
    if request.GET.get('next'):
        referer = request.GET.get('next')
    else:
        referer = request.META.get('HTTP_REFERER', reverse(reverse_url))
    return referer.replace(remove, '')
