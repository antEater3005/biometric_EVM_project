from django.contrib import admin
from django.urls import path
from .views import CreateElection, HomePage, AddConstituency, AddCandidate, get_constituencies, ShowCandidate, AddVoter
urlpatterns = [
    path('', HomePage, name='home'),
    path('CreateElection/', CreateElection, name='create_election'),
    path('addConstituency/', AddConstituency, name='add-constituency'),
    path('addCandidate/', AddCandidate, name='add-candidate'),
    path('get_constituencies/', get_constituencies, name='get_constituencies'),
    path('candi_details/', ShowCandidate, name='candi_details'),
    path('add_voter/', AddVoter, name='add_voter')
]
