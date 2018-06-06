from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    texts = ['First django app ever']
    context = {
        'title': 'Django E-Commerce',
        'texts': texts
    }
    return render(request, "index.html", context)
