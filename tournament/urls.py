from django.urls import path
from . import views

urlpatterns = [
    path('tournaments/stats/', views.tournament_chart, name='tournament_chart'),
    path('tournaments/new/', views.new_tournament, name='new_tournament'),
    path('tournaments/', views.create_tournament, name='create_tournament'),
]
