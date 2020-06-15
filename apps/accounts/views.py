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


class UserProfileView(LoginRequiredMixin, generic.UpdateView):
    model = UserProfile
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('profile')

    def get(self, request, **kwargs):
        self.object = UserProfile.objects.get(id=self.request.user.id)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_form_class(self):
        return UserProfileForm

    def get_object(self, queryset=None):
        return UserProfile.objects.get(id=self.request.user.id)

    # def get_success_url(self):
    #     view_name = 'update_mymodel'
    #     return reverse_lazy(view_name, kwargs={'model_name_slug': self.kwargs.get('model_name_slug','')})

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     # self.object.user = UserProfile.objects.get(id=self.request.user.id)
    #     # self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     self.object = form.save()
    #     return response
    def form_valid(self, form):
        form.save(self.request.user)
        return super(UserProfileView, self).form_valid(form)


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'accounts/profile.html')
