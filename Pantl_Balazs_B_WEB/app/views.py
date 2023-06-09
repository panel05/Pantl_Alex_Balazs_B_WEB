from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .filters import *


def szavak(request):
    szavak = Szavak.objects.all()

    szavakFilter = TemaFilter(request.GET, queryset = szavak)

    context = {
        'szavak' : szavak,
        'szavakFilter' : szavakFilter
    }

    return render(request, 'szavak.html', context=context)


def tema(request, temaId):
    Szavak.objects.filter(Tema__temaId = temaId)

    context = {
        'tema' : tema,
        'szavak' : szavak
    }

    return render(request,"app/tema.html", context=context)
