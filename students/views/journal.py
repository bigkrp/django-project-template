# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from datetime import datetime
from calendar import monthrange
from calendar import month_name
from calendar import day_name

def visiting_list(request):
    year = 2019
    month = 11
    days = monthrange(year, month)[1]
    curent_month = month_name[month]
    resultDays = []

    resultDays = map(lambda day: formatDays(day, month, year), range(1, days + 1))

    return render(request, 'students/visiting.html', {
        'days': resultDays,
        'month': curent_month,
        'year': year
    })

def formatDays(day, month, year):
    return findDay(str(day) + ' ' + str(month) + ' ' + str(year)) + ' ' + str(day)

def findDay(date):
    date = datetime.strptime(date, '%d %m %Y')
    return date.strftime('%a')