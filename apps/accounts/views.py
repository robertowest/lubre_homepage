# from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.http import urlencode
from django.shortcuts import get_object_or_404, redirect, render

from apps.empresa.models import Comercial

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def LoginRedirect(request):
    if request.user is not None and request.user.is_active:
        if request.user.is_superuser:
            return HttpResponseRedirect("/admin/")
        elif request.user.is_staff:
            # si el empleado es un comercial, enviamos hacia otro destino
            # comercial = get_object_or_404(Comercial, usuario=request.user)
            try:
                comercial = Comercial.objects.get(usuario=request.user)

                if comercial:
                    # return HttpResponseRedirect("/comercial/")
                    # return HttpResponseRedirect("/empresa/recorrer/")
                    # return HttpResponseRedirect("/empresa/filtro_comercial/" + str(comercial.id))
                    get_args_str = urlencode({'comercial': comercial.id, 'active': True})
                    return HttpResponseRedirect("/empresa/listado/?%s" % get_args_str)
                else:
                    return HttpResponseRedirect("/empleado/")

            except Comercial.DoesNotExist:
                return HttpResponseRedirect("/empleado/")
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
            # messages.success(request, 'Inicio de seción exitoso')
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
            # messages.success(request, f'Su cuenta fue creada correctamente.')
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'accounts/signup.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    user_profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'accounts/profile.html', {'object': user_profile})
