from django.urls import path
from . import views

urlpatterns = [
    path('tournaments/stats/', views.tournament_chart, name='tournament_chart')
]
