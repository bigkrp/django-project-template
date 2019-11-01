# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from calendar import monthrange
from calendar import month_name

def visiting_list(request):
    year = 2018
    range = monthrange(year, 10)
    curent_month = month_name[10]

    return render(request, 'students/visiting.html', {
        'range': range,
        'month': curent_month,
        'year': year
    })
