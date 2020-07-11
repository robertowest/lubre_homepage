from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def LoginRedirect(request):
    if request.user is not None and request.user.is_active:
        if request.user.is_superuser:
            return HttpResponseRedirect("/admin/")
        elif request.user.is_staff:
            # return HttpResponseRedirect("/tienda/")
            return HttpResponseRedirect("/cartera/")
        else:
            return HttpResponseRedirect("/")


def login_view(request):
    if request.method == 'POST':
        userinput = request.POST['username']
        try:
            username = User.objects.get(email=userinput).username
        except User.DoesNotExist:
            username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Inicio de seción exitoso')
            return redirect('redirect')
        else:
            messages.error(request, 'Datos incorrectos, por favor verifique usuario/correo o contraseña.')
    return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
            username = form.cleaned_data.get('username')
            messages.success(request, f'Su cuenta fue creada correctamente.')
            return redirect('login')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})


# # the decorator: To access the profile page, users should login
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UserUpdateForm(request.POST, instance=request.user)
#         profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, f'Sus datos fueron actualizados correctamente.')
#             return redirect('profile')
#     else:
#         user_form = UserUpdateForm(instance=request.user)
#         profile_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'u_form': user_form,
#         'p_form': profile_form,
#         'object': Profile.objects.get(user_id=request.user.id),
#     }
#
#     return render(request, 'accounts/profile.html', context)

@login_required(login_url='/accounts/login/')
def profile(request):
    # if request.method == 'POST':
    #     user_form = UserForm(request.POST, instance=request.user)
    #     profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    # else:
    #     # context = {'object': User.objects.get(id=request.user.id)}
    # return render(request, 'accounts/profile.html', context)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    user_profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'accounts/profile.html', {'object': user_profile})
