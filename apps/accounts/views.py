from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic


# Create your views here.
class SignUpTemplateView(generic.TemplateView):
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('top')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=user, password=password)

            from django.core.mail import send_mail
            # (subject, message, from_email, recipient_list)
            send_mail('nuevo usuario registrado', 
                      'se registró el usuario {}'.format(username),
                      'homepage@lubresrl.com.ar', ['info@lubresrl.com.ar'])

            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('signup'))


def LoginRedirect(request):
    if request.user is not None and request.user.is_active:
        if request.user.is_superuser:
            return HttpResponseRedirect("/admin/")    
        elif request.user.is_staff:
            # return HttpResponseRedirect("/tienda/")
            return HttpResponseRedirect("/cartera/")
        else:
            return HttpResponseRedirect("/")
