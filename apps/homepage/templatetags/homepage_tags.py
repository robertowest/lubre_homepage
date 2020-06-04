from django import template

from django.conf import settings
import os.path

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)


@register.filter(name='color')
def color(value):
    tipo = value.split('|')[1]
    if tipo == 'distri':
        return "#a6c4a6"
    elif tipo == 'eess':
        return "#aacbe5;"


@register.filter(name='product_path')
def product_path(value):
    path = settings.MEDIA_ROOT + 'product/'
    file = str(value).zfill(5) + '.jpg'

    import pdb;
    pdb.set_trace()

    # if os.path.isfile(path + file):
    if os.path.exists(path + file):
        return path + file
    else:
        return path + 'none.jpg'


@register.filter(name='thumb_product_path')
def thumb_product_path(value):
    """Agregar thumb/ a la ruta de la imagen"""
    return str(value.name).replace('product/', 'product/thumb/')


@register.filter
def greeting_to_time(user):
    import datetime, pytz
    from django.conf import settings

    if user.first_name:
        name = user.first_name
        if user.last_name:
            name = name + ' ' + user.last_name
    else:
        name = user.username

    cur_time = datetime.datetime.now(tz=pytz.timezone(str(settings.TIME_ZONE)))
    if cur_time.hour < 12:
        return 'Buenos días {}'.format(name)
    elif cur_time.hour < 20:
        return 'Buenas tardes {}'.format(name)
    else:
        return 'Buena noches {}'.format(name)
