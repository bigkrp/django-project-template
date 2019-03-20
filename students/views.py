# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Views for students

def students_list(request):
    """Return students list"""
    return render(request, 'students/students_list.html', {})

def students_add(request):
    """Add new student"""
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    """Edit student"""
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    """Delete student"""
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for groups

def groups_list(request):
    """Return group list"""
    return HttpResponse('<h1>Group Listing</h1>')

def groups_add(request):
    """Add new student"""
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    """Edit group"""
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    """Delete group"""
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)