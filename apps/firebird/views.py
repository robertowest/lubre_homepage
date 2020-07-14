# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def cartera(request):
    # labels = []
    # data = []
    #
    # labels.append('Combustible')
    # data.append('55')
    #
    # labels.append('Lubricante')
    # data.append('30')
    #
    # labels.append('Otros')
    # data.append('15')

    area_chart_labels, area_chart_data = area_chart()
    pie_chart_labels, pie_chart_data = pie_chart()
    context = {
        'area_chart_labels': area_chart_labels,
        'area_chart_data': area_chart_data,
        'pie_chart_labels': pie_chart_labels,
        'pie_chart_data': pie_chart_data,
    }
    return render(request, 'dashboard.html', context)


def area_chart():
    labels = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    data = [0, 10000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 40000]
    return labels, data


def pie_chart():
    labels = []
    data = []

    labels.append("Combustible")
    data.append("55")

    labels.append("Lubricante")
    data.append("30")

    labels.append("Otros")
    data.append("15")

    return labels, data
