# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'Мтм-1',
         'leader': {'id': 1, 'name': u'Тарас Мельник'}},

        {'id': 1,
         'name': u'Мтм-22',
         'leader': {'id': 2, 'name': u'Микола Садовський'}},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    """Add new student"""
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    """Edit group"""
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    """Delete group"""
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
