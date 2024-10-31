from django.urls import path
from app.views.test import TestView
from app.views.search import SearchView
from app.views.typeData import TypeDataView

urlpatterns = [
    path('test/', TestView.as_view()),
    path('search/', SearchView.as_view()),
    path('typedata/', TypeDataView.as_view()),
]
