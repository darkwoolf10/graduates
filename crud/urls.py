from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('statistic', views.statistic, name='statistic'),
    path('curators', views.curators, name='curators'),
    path('curator/create', views.create_curator, name='create-curator'),
]