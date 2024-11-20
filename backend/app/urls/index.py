from django.urls import path
from app.views.test import TestView
from app.views.search import SearchView
from app.views.typeData import TypeDataView
from app.views.speciesDetail import SpeciesDetailView
from app.views.geneDetail import GeneDetailView
from app.views.experimental import ExpermentalView
from app.views.counter import CounterView
from app.views.pathway_imgs import PathwayView
from app.views.disease import DiseaseView
from app.views.stress import StressView
from app.views.suggestion import SuggestionView

urlpatterns = [
    path('test/', TestView.as_view()),
    path('search/', SearchView.as_view()),
    path('typedata/', TypeDataView.as_view()),
    path('speciesdetail/', SpeciesDetailView.as_view()),
    path('genedetail/', GeneDetailView.as_view()),
    path('experimental/', ExpermentalView.as_view()),
    path('counter/', CounterView.as_view()),
    path('pathway/', PathwayView.as_view()),
    path('disease/', DiseaseView.as_view()),
    path('stress/', StressView.as_view()),
    path('suggestion/', SuggestionView.as_view()),
]
