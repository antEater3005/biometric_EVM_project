from django.contrib import admin
from django.urls import path
from .views import CreateElection, HomePage
urlpatterns = [
    path('', HomePage, name='home'),
    path('CreateElection/', CreateElection, name='create_election')

]
