from __future__ import unicode_literals
from django.shortcuts import render
from products.models import Product


def products(request):
    return render(request, 'products/categories.html')

# Product.objects.filter() will find all the product entries from the database whose category is audio
# We then assign them to a 'products_list' variable and send that variable to audio.html template
def audio(request):
    return render(request, 'products/audio.html', {'products_list': Product.objects.filter(category='audio')})

def control(request):
    return render(request, 'products/control.html', {'products_list': Product.objects.filter(category='control')})

def interactive(request):
    return render(request, 'products/interactive.html', {'products_list': Product.objects.filter(category='interactive')})

def visual(request):
    return render(request, 'products/visual.html', {'products_list': Product.objects.filter(category='visual')})