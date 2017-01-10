from django.conf.urls import url

from . import views

app_name = 'flora'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<plant_id>[0-9]+)/$', views.plante, name='plante'),
    url(r'^planteliste/', views.planteliste, name='planteliste'),
    url(r'^familieliste/', views.familieliste, name='familieliste'),
    url(r'^search/', views.search, name='search'),
    url(r'^familie/', views.familie, name='familie'),
    url(r'^famile_latin/', views.familieliste_latin, name='familieliste_latin'),
    url(r'^slide/', views.slide, name='slide'),
]
