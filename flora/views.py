from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Plant
import math

def index(request):
    return render(request, 'flora/index.html')

def planteliste(request):
    pl = Plant.objects.all().order_by('norwegian_name')
    n = math.ceil(pl.count()/3.0)
    splitListe = [pl[i:i+int(n)] for i in xrange(0, len(pl), int(n))]
    context = {
        'splitListe0': splitListe[0],
        'splitListe1': splitListe[1],
        'splitListe2': splitListe[2],
    }
    return render(request, 'flora/planteliste.html', context)

def familieliste(request):
    familieliste = []
    planteliste = Plant.objects.all()
    for plant in planteliste:
        familieliste.append(plant.norwegian_family)
    familieliste = set(familieliste)
    familieliste = sorted(familieliste)
    context = {
        'familieliste': familieliste
    }
    return render(request, 'flora/familieliste.html', context)

def familieliste_latin(request):
    familieliste = []
    planteliste = Plant.objects.all()
    for plant in planteliste:
        familieliste.append(plant.latin_family)
    familieliste = set(familieliste)
    familieliste = sorted(familieliste)
    context = {
        'familieliste': familieliste
    }
    return render(request, 'flora/familieliste.html', context)

def plante(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    pictures = plant.picture_set.all()
    context = {
        'plant': plant,
        'pictures': pictures,
    }
    return render(request, 'flora/detail.html', context)

def search(request):
    searchText = request.POST.get("search")
    result = Plant.objects.filter(norwegian_name__iexact=searchText)
    result = result | Plant.objects.filter(norwegian_family__iexact=searchText)
    result = result | Plant.objects.filter(latin_family__iexact=searchText)
    context = {
        'result': result,
        'searchText': searchText,
    }
    return render(request, 'flora/search.html', context)

def familie(request):
    path = request.path
    pathEnd = path.split("/")
    pathLength = len(pathEnd)
    searchText = pathEnd[pathLength-1]
    result = Plant.objects.filter(norwegian_family__iexact=searchText)
    result = result | Plant.objects.filter(latin_family__iexact=searchText)
    context = {
        'result': result,
        'searchText': searchText,
    }
    return render(request, 'flora/search.html', context)

def kontakt(request):
    return render(request, 'flora/kontakt.html')

def slide(request):
    path = request.path
    pathEnd = path.split("/")
    pathLength = len(pathEnd)
    searchText = pathEnd[pathLength-2]
    plant = Plant.objects.get(pk=searchText)
    pictures = plant.picture_set.all()
    firstPic = pictures.first()
    context = {
        'plant': plant,
        'pictures': pictures,
        'firstPic': firstPic,
    }
    return render(request, 'flora/slide.html', context)
