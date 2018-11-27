from __future__ import unicode_literals
from django.shortcuts import render


def get_index(request):
    return render(request, 'index.html')

def get_about(request):
    return render(request, 'about.html')