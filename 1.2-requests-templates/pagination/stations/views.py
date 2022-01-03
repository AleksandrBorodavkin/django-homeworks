import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page_number', 1))
    with open('data-398-2018-08-30.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        obj = [row for row in reader]
        paginator = Paginator(obj, 10)
        page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
