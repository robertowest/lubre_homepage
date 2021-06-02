from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect, request
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from . import models

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'homepage/index.html'

    def get_context_data(self, **kwargs):
        # context['pages'] = models.Entries.objects.filter(section='home').filter(active=1).order_by('ordered')
        # context['about'] = models.Entries.objects.filter(section='about').filter(active=1).order_by('ordered')
        # context['whyus'] = models.Entries.objects.filter(section='whyus').filter(active=1).order_by('ordered')
        # context['service'] = models.Entries.objects.filter(section='service').filter(active=1).order_by('ordered')
        # context['staff'] = User.objects.filter(is_staff=True)
        # context['cataTag'] = models.Entries.objects.filter(section='cataTag').filter(active=1).order_by('ordered')
        # context['catalog'] = models.Entries.objects.filter(section='catalog').filter(active=1).order_by('ordered')
        # context['message'] = models.Entries.objects.filter(section='message').filter(active=1).order_by('ordered')
        # context['post'] = models.Post.objects.filter(publish_on__isnull=False).order_by('-publish_on')[:3]

        context = super().get_context_data(**kwargs)
        context['pages'] = models.Entries.objects.filter(section='home').filter(active=1).order_by('ordered')

        for reg in context['pages']:
            if reg.text_short:
                _section = reg.text_short[1:]

                if _section == 'about':
                    context['about'] = models.Entries.objects.filter(section='about').filter(active=1).order_by('ordered')
                    context['whyus'] = models.Entries.objects.filter(section='whyus').filter(active=1).order_by('ordered')

                if _section == 'catalog':
                    context['cataTag'] = models.Entries.objects.filter(section='cataTag').filter(active=1).order_by('ordered')
                    context['catalog'] = models.Entries.objects.filter(section='catalog').filter(active=1).order_by('ordered')

                # primera opción de servicios
                # if _section == 'service':
                #     context['service'] = models.Entries.objects.filter(section='service').filter(active=1).order_by('ordered')

                # segunda opción de servicios
                # if _section == 'service':
                #     context['dist'] = [
                #             {'categoria': 5,  'icono': 'lubricante',         'texto': 'Combustibles y Lubricantes'},
                #             {'categoria': 6,  'icono': 'fertilizante',       'texto': 'Fertilizantes<br><br>'},
                #             {'categoria': 2,  'icono': 'proteccion-cultivo', 'texto': 'Protección de Cultivos'},
                #             {'categoria': 11, 'icono': 'silo-bolsa',         'texto': 'Silo Bolsa<br><br>'},
                #     ]
                #     context['eess'] = [
                #             {'categoria': 68, 'icono': 'combustible', 'texto': 'Combustibles'},
                #             {'categoria': 69, 'icono': 'coffee',      'texto': 'YPF Full'},
                #             {'categoria': 70, 'icono': 'boxes',       'texto': 'YPF Boxes'},
                #             {'categoria': 71, 'icono': 'serviclub',   'texto': 'ServiCLUB'},
                #     ]

                if _section == 'servicesCatalog':
                    context['scLabel'] = models.Entries.objects.filter(section='scLabel').filter(active=1).order_by('ordered')
                    context['serviceCatalog'] = models.Entries.objects.filter(section='serviceCatalog').filter(active=1).order_by('ordered')

                if _section != 'home':
                    context[_section] = models.Entries.objects.filter(section=_section).filter(active=1).order_by('ordered')

        context['post'] = models.Post.objects.filter(publish_on__isnull=False).order_by('-publish_on')[:3]
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # envío de correo
        # body = render_to_string(
        #     'email_content.html',
        #     {
        #         'name': name,
        #         'email': email,
        #         'subject': subject,
        #         'message': '<br />'.join(message.splitlines()),   # reemplazamos los saltos de línea por html
        #     },
        # )
        # send_mail = EmailMessage(
        #     subject = subject,
        #     body = body,
        #     from_email = email,
        #     to = ['roberto.west@gmail.com']
        # )
        # send_mail.content_subtype = 'html'
        # try:
        #     send_mail.send()
        # except BadHeaderError:
        #     return HttpResponse('Invalid header found.')
        mensaje = models.Mensaje()
        mensaje.nombre = name
        mensaje.correo = email
        mensaje.asunto = subject
        mensaje.mensaje = message
        mensaje.save()

        return HttpResponseRedirect(reverse('homepage:homepage'))


class PostList(generic.ListView):
    model = models.Post
    template_name = 'blog/index.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['pages'] = models.Entries.objects.filter(section='home').filter(active=1).order_by('ordered')
        context['categories'] = models.Category.objects.all()
        return context

    def get_queryset(self):
        queryset = super(PostList, self).get_queryset()
        return queryset.filter(publish_on__isnull=False).order_by('-publish_on')


class PostDetail(generic.DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['recents'] = models.Post.objects.filter(publish_on__isnull=False).order_by('-publish_on')[:3]
        return context


class ServiceDetail(generic.DetailView):
    model = models.Entries
    template_name = 'service/service_detail.html'


class TemplateView(generic.TemplateView):
    template_name = 'accounts/register.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            user = User.objects.create_user(username, email, password)
            user.save()
            user = authenticate(username=user, password=password)
            #login
            return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('register'))


class CategoriaListView(generic.ListView):
    model = models.Grupo
    template_name = 'grupo/grupo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        try:
            categoria_id = self.kwargs['pk']
        except:
            categoria_id = None

        grupos = None
        productos = None

        if categoria_id:
            grupos = models.Grupo.objects.filter(activo=1).filter(categoria=categoria_id)
            productos = models.Producto.objects.filter(activo=1).filter(grupo__in=grupos)

        context = {
            'grupos': grupos,
            'productos': productos,
            'pages': models.Entries.objects.filter(section='home').filter(active=1).order_by('ordered')
        }
        return context


class ProductoDetail(generic.DetailView):
    model = models.Producto
    template_name = 'grupo/producto_detail.html'


class BusquedaListView(generic.ListView):
    model = models.Producto
    template_name = 'grupo/producto_list.html'

    def post(self, request, *args, **kwargs):
        busqueda = request.POST.get("producto")
        productos = models.Producto.objects.filter(activo=1).filter(nombre__icontains=busqueda)
        return render(request, self.template_name, {'productos': productos})
