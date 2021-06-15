from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from django.core.mail import BadHeaderError, EmailMessage
from django.template.loader import render_to_string

from apps.homepage.models import Entries, Grupo, Producto


class IndexView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # opciones de servicios
        context['agro'] = [
            {'texto': 'Lubricantes',   'imagen': 'img/landing/lubricante.svg',   'categoria': 5},
            {'texto': 'Combustibles',  'imagen': 'img/landing/combustible.svg',  'categoria': 1},
            {'texto': 'Fertilizantes', 'imagen': 'img/landing/fertilizante.svg', 'categoria': 6},
            {'texto': 'Cultivos',      'imagen': 'img/landing/cultivo.svg',      'categoria': 2},
            {'texto': 'Silo Bolsa',    'imagen': 'img/landing/silo.svg',         'categoria':11},
            {'texto': 'Semillas',      'imagen': 'img/landing/semilla.svg',      'categoria':12},
        ]
        context['eess'] = [
            {'texto': 'Combustible', 'imagen': 'img/landing/surtidor.svg',  'categoria': 68, 
             'descripcion': 'Diseñados para lograr el máximo desempeño, excelente poder de limpieza y óptimo rendimiento.'},
            {'texto': 'Full',        'imagen': 'img/landing/coffee.svg',    'categoria': 69, 
             'descripcion': 'Red con cobertura nacional ubicados en estaciones de servicio YPF.'},
            {'texto': 'Boxes',       'imagen': 'img/landing/tools.svg',     'categoria': 70, 
             'descripcion': 'Espacio de encuentro y permanencia placentera.'},
            {'texto': 'Serviclub',   'imagen': 'img/landing/serviclub.svg', 'categoria': 71, 
             'descripcion': 'Programa de fidelización de clientes en las estaciones de servicio YPF.'},
        ]
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        name = request.POST.get('name')
        phone = request.POST.get('subject')
        subject = "enviado desde la web"
        message = request.POST.get('message')

        message = message +  \
                  "\n\nNombre: " + name + \
                  "\nCorreo: " + email + \
                  "\Teléfono: " + phone

        # # grabamos el mensaje en la tabla
        # from apps.homepage.models import Mensaje
        # mensaje = Mensaje()
        # mensaje.nombre = name
        # mensaje.correo = email
        # mensaje.asunto = "contacto desde la web"
        # mensaje.mensaje = message
        # mensaje.save()

        # envío de correo
        body = render_to_string(
            'email_content.html',
            {
                'name': name,
                'email': email,
                'subject': subject,
                'message': '<br />'.join(message.splitlines()),   # reemplazamos los saltos de línea por html
            },
        )
        send_mail = EmailMessage(
            subject = subject,
            body = body,
            from_email = email,
            to = ['roberto.west@gmail.com']
        )
        send_mail.content_subtype = 'html'
        try:
            send_mail.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

        return HttpResponseRedirect(reverse('landing:index'))


class CategoriaListView(ListView):
    model = Grupo
    template_name = 'landing/categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        try:
            categoria_id = self.kwargs['pk']
        except:
            categoria_id = None

        grupos = None
        productos = None

        if categoria_id:
            grupos = Grupo.objects.filter(activo=1).filter(categoria=categoria_id)
            productos = Producto.objects.filter(activo=1).filter(grupo__in=grupos)

        context = {
            'grupos': grupos,
            'productos': productos
        }
        return context


class ProductoDetail(DetailView):
    model = Producto
    template_name = 'landing/producto_detalle.html'     # grupo/producto_detail.html


class ServicioDetail(DetailView):
    model = Entries
    template_name = 'landing/servicio_detalle.html'     # service/service_detail.html
