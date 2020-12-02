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


def redirect_with_params(request, to, *args, **kwargs):
def redirect_to_with_next(request, reverse_url, type="GET", *args, **kwargs):
    # si existe la directiva "next", la recupera pa volver a pasarla como parámetro a "reverse_url"
    if (type == "GET"):
        redirect_to = request.GET.get('next')
    else:
        redirect_to = request.POST.get('next')

    # return HttpResponseRedirect(reverse(reverse_url, kwargs={'next': redirect_to}))
    return render()


def get_url_referer(request):
    remove = request._current_scheme_host
    referer = request.META['HTTP_REFERER']
    return referer.replace(remove, '')
