from django.http import HttpResponse
from django.shortcuts import render
from .models import Catalog
# import paginator
from .utils import get_paginated_objects


def index(request):
    """main page"""
    

    return render(request, "catalog/index.html")


def catalog(request):
    context = get_paginated_objects(Catalog.objects.all(), request)
    return render(request, 'catalog/catalog.html', context)


def catalog_detail(request, pk):
    return render(request, 'catalog/catalog_detail.html')
