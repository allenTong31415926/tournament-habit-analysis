from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.tournament_chart, name='tournament_chart')
]
