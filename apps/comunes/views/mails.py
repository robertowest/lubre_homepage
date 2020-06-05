from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def test_send_mail(request):
    subject = request.POST.get('subject', 'send_mail')
    message = request.POST.get('message', 'mensaje enviado utilizando send_mail')
    from_email = request.POST.get('from_email', 'info@lubresrl.com.ar')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['roberto.west@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Encabezado inválido.')
        # return HttpResponseRedirect('/contact/thanks/')
        return HttpResponse('Mensaje enviado correctamente.')
    else:
        return HttpResponse('Asegúrese que todos los campos estén ingresados ​​y sean válidos.')


from django.template import loader
from django.contrib.auth.models import User

def test_send_mail_template(request):
    subject = request.POST.get('subject', 'Gracias por usar email')
    message = request.POST.get('message', 'Mensaje enviado utilizando send_mail')
    from_email = request.POST.get('from_email', 'info@lubresrl.com.ar')
    html_message = loader.render_to_string(
                        'mails/ejemplo.html',
                        {
                            # config
                            'logo_url': 'http://lubresrl.com.ar/static/faviicon.png',
                            'footer_content': '<p>Ruta 9 km 1306 - T4101 Los Nogales - Tucuman, Argentina</p>',
                            'facebook_url': 'https://www.facebook.com/lubresrl.ypfagro/',
                            'twitter_url': 'https://ar.linkedin.com/company/lubre-srl',
                            'instagram_url': 'https://www.instagram.com/lubresrl.ypfagro/',
                            'website_url': 'http://lubresrl.com.ar',
                            # css
                            'color_header_bg': '#f7f7f7',
                            'color_title': '#222222',
                            'title_size': 'h1',
                            'color_body_bg': '#ffffff',
                            'color_body': '#808080',
                            'color_body_link': '#007e9e',
                            'color_button': '#ffffff',
                            'color_button_bg': '#00add8',
                            'border_radius_button': '3',
                            'color_footer': '#ffffff',
                            'color_footer_link': '#ffffff',
                            'color_footer_bg': '#333333',
                            'color_footer_divider': '#505050',
                            # data
                            'subject': subject,
                            'title': 'Título',
                            'body': message,
                            'banner_url': 'http://lubresrl.com.ar/static/img/ypf_agro.png',
                            'button_link': 'http://lubresrl.com.ar/',
                            'button_label': 'Lubre SRL',
                            # custom
                            'user_name': 'Usuario',     # User.username,
                        }
                   )
    try:
        send_mail(subject, message, from_email, ['roberto.west@gmail.com'], 
                fail_silently=True, html_message=html_message
        )
        return HttpResponse('Mensaje enviado correctamente.')
    except BadHeaderError:
        return HttpResponse('Asegúrese que todos los campos estén ingresados ​​y sean válidos.')


# django-templated-email
from templated_email import send_templated_mail

def test_simple_mail(request):

    try:
        send_templated_mail(
            template_name='welcome',
            from_email='info@lubresrl.com.ar',
            recipient_list=['roberto.west@gmail.com'],
            context={
                'username': request.user.username,
                'full_name': request.user.get_full_name(),
                'signup_date': request.user.date_joined
            },
            # Optional:
            # cc=['cc@example.com'],
            # bcc=['bcc@example.com'],
            # headers={'My-Custom-Header':'Custom Value'},
            # template_prefix="my_emails/",
            # template_suffix="email",
        )
        return HttpResponse('Mensaje enviado correctamente.')
    except BadHeaderError:
        return HttpResponse('Asegúrese que todos los campos estén ingresados ​​y sean válidos.')
