import django_filters as filters
from django import forms
from .models import *

class TemaFilter(filters.FilterSet):
    temaId = filters.ModelChoiceFilter(
        label = 'Téma',
        field_name = 'tema_id',
        queryset = Tema.objects.all(),
        widget = forms.Select(attrs = {'class' : 'form-control'})
    )

class Meta:
    model = Szavak
    fields = ['temaId']