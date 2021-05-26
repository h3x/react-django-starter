from django.shortcuts import render


def index(request, *args, **kw):
    return render(request, 'frontend/index.html')
