from django.shortcuts import render


def bad_request(request):
    context = {}
    return render(request, 'errores/400.html', context, status=400)


def permission_denied(request):
    context = {}
    return render(request, 'errores/403.html', context, status=403)


def page_not_found(request):
    context = {}
    return render(request, 'errores/404.html', context, status=404)


def server_error(request):
    context = {}
    return render(request, 'errores/500.html', context, status=500)
