from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Elections model


class Election(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    no_of_constituencies = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    type_of_election = models.CharField(max_length=100)


# Constituency model
class Constituency(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type_of_constituency = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    number_of_candidates = models.IntegerField()
    district_name = models.CharField(max_length=100)
    no_candidates = models.IntegerField()


# Candidates Model
class Candidates(models.Model):
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    party_name = models.CharField(max_length=100)
    candidate_symbol = models.ImageField()
    photo = models.ImageField()
    total_votes = models.IntegerField()
