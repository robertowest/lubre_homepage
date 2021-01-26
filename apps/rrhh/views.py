from datetime import datetime, timedelta
from bootstrap_modal_forms.generic import BSModalReadView
from django.db.models import Q, When
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone

from . import models


def home(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    # vencimientos = Documentacion.objects.all()  # filter('dias_vencido': 0)

    # Model.objects.filter(Q(x=1) & Q(y=2))  AND
    # Model.objects.filter(Q(x=1) | Q(y=2))  OR
    # Q(name__startswith="John") | Q(name__startswith="Paul")
    # vencimientos = Documentacion.objects.filter(Q(dias_vencido='0'))

    # proximos vencimientos (7 días)
    f1 = Q(proximo__range=(timezone.now() + timedelta(days=1),
                           timezone.now() + timedelta(days=7)))
    f2 = Q(fecha_final__range=(timezone.now() + timedelta(days=1),
                               timezone.now() + timedelta(days=7)))
    proximos = models.Mantenimiento.objects.filter(f1 | f2)

    # vencidas
    v1 = Q(proximo__lt=timezone.now()) | Q(fecha_final__lt=timezone.now())
    vencimientos = models.Mantenimiento.objects.filter(v1)

    # estado en rojo o amarillo
    mantenimientos = models.Mantenimiento.objects.filter(Q(estado='R') | Q(estado='A'))

    # noticias = Post.objects.all().order_by('-created')
    noticias = None  # Post.objects.filter(estado=1).order_by('-created')

    return render(request, 'rrhh/index.html', {'proximos': proximos,
                                               'vencimientos': vencimientos,
                                               'mantenimientos': mantenimientos,
                                               'noticias': noticias})
