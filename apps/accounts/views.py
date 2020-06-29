from django.db import transaction
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from apps.comunes.views.mails import signup_mail
from .models import UserProfile
from .forms import UserForm, UserProfileForm

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


from django.http import HttpResponse, HttpResponseRedirect, request

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/profile2.html', {
        'user_form': user_form,
        'profile_form': profile_form}
    )
