from django.urls import path
from .views import startElection

urlpatterns = [
    path('', startElection, name='start-election'),
    path('', startElection, name='election_details'),

]
