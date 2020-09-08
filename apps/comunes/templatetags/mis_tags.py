from django import template
from django.db.models.query import QuerySet

register = template.Library()


# @register.filter
# def appname(obj):
#     # 'app_label': model._meta.app_label,
#     # 'model_name': model._meta.object_name.lower()
#     try:
#         # if isinstance(obj, Model):
#         #     return obj.get_app_label
#         return model._meta.app_label
#     except:
#         return 'unknow_app'


@register.filter
def verbose_name(obj):
    if isinstance(obj, QuerySet):
        return obj.model._meta.verbose_name
    else:
        return obj._meta.verbose_name


@register.filter
def verbose_name_plural(obj):
    # return obj._meta.verbose_name_plural
    # return obj.__class__.__name__         obj.query.base_table
    if isinstance(obj, QuerySet):
        return obj.model._meta.verbose_name_plural
    else:
        return obj._meta.verbose_name_plural


@register.filter
def filtro_active(modelo, valor):
    return modelo.filter(active=valor)


@register.filter
def query(qs, **kwargs):
    """ template tag which allows queryset filtering. Usage:
          {% query books author=author as mybooks %}
          {% for book in mybooks %}
            ...
          {% endfor %}
    """
    return qs.filter(**kwargs)


@register.filter
def url_action(obj, action):
    if isinstance(obj, QuerySet):
        model_name = obj.model._meta.verbose_name
    else:
        model_name = obj._meta.verbose_name
    return '{obj}:{act}'.format(obj=model_name.lower(), act=action.lower())


@register.filter
def url_action_pk(url, pk):
    return '{url} {id}'.format(url=url, id=pk)


@register.simple_tag()
def var_dump(var):
    # forma de uso en html: {% var_dump VARIABLE %}
    return vars(var)


@register.filter
def file_exists(value):
    try:
        template.loader.get_template(value)
        return True
    except template.TemplateDoesNotExist:
        return False


@register.filter
def build_url(value, args):
    if args is None:
        return value
    arg_list = [arg.strip() for arg in args.split(',')]
    return value + "?" + arg_list[0] + "=" + arg_list[1]


@register.filter
def addstr(value, arg):
    if arg is None:
        arg = 0
    return str(value) + str(arg)
