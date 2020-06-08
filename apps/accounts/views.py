from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from apps.comunes.views.mails import signup_mail
from . import forms

# Create your views here.
def LoginRedirect(request):
    if request.user is not None and request.user.is_active:
        if request.user.is_superuser:
            return HttpResponseRedirect("/admin/")    
        elif request.user.is_staff:
            # return HttpResponseRedirect("/tienda/")
            return HttpResponseRedirect("/cartera/")
        else:
            return HttpResponseRedirect("/")


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

            # # (subject, message, from_email, recipient_list)
            # from django.core.mail import send_mail
            # send_mail('nuevo usuario registrado', 
            #           'se registró el usuario {}'.format(username),
            #           'homepage@lubresrl.com.ar', ['info@lubresrl.com.ar'])
            signup_mail(to=user.email, username=user.username, joined=user.date_joined)
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('signup'))


class ProfileView(generic.TemplateView):
    model = User
    template_name = 'accounts/profile.html'
    def get_object(self):
        return self.request.user
        
# class ProfileView(generic.UpdateView):
#     model = User
#     form_class = forms.User
#     template_name = 'accounts/profile.html'

#     def get_object(self):
#         return self.request.user


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'accounts/profile.html')
