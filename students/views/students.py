# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 235,
         'image': 'img/building.jpg'},
        {'id': 2,
         'first_name': u'Корост',
         'last_name': u'Андрій',
         'ticket': 2123,
         'image': 'img/mountains.jpg'},
        {'id': 3,
         'first_name': u'Притула',
         'last_name': u'Тарас',
         'ticket': 666,
         'image': 'img/man.jpg'}
    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    """Add new student"""
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    """Edit student"""
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    """Delete student"""
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
