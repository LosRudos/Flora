#!/usr/bin/python

import pyexcel as pe
import psycopg2
import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "floraRuden.settings")
django.setup()

from flora.models import Plant

sheet = pe.get_sheet(file_name="testliste.ods")

for i in sheet.rows():
    nn = i[5]
    lf = i[6]
    nf = i[7]
    nnlen = len(nn)
    print(nnlen)
    exists = Plant.objects.filter(norwegian_name=nn).count()
    if (exists == 0 and nnlen > 2):
        p = Plant(norwegian_name=nn, latin_family=lf, norwegian_family=nf)
        p.save()
#    print(type(nn))
#    print("norsk navn = ", nn)


# Telle antall planter i databasen:
# >>> nr = Plant.objects.filter().count()
# >>> print(nr)

