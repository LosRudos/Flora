#!/usr/bin/python

import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "floraRuden.settings")
django.setup()

from flora.models import Plant

familieliste = []
planteliste = Plant.objects.all()

for plante in planteliste:
    familieliste.append(plante.norwegian_family)

print(familieliste[2])
