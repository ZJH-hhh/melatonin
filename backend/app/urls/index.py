from django.urls import path
from app.views.test import TestView
from app.views.search import SearchView
from app.views.typeData import TypeDataView
from app.views.speciesDetail import SpeciesDetailView
from app.views.geneDetail import GeneDetailView
from app.views.experimental import ExpermentalView
from app.views.counter import CounterView

urlpatterns = [
    path('test/', TestView.as_view()),
    path('search/', SearchView.as_view()),
    path('typedata/', TypeDataView.as_view()),
    path('speciesdetail/', SpeciesDetailView.as_view()),
    path('genedetail/', GeneDetailView.as_view()),
    path('experimental/', ExpermentalView.as_view()),
    path('counter/', CounterView.as_view()),
]
