from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ElectionForm, AddConstituencyForm, AddCandidateForm, AddVoterForm
from .models import Constituency, Election, Candidates, Voters
# Create your views here.


def CreateElection(request):
    form = ElectionForm()

    if request.method == 'POST':
        form = ElectionForm(request.POST)
        if form.is_valid():
            form.save()
            form = ElectionForm()
            return redirect('home')

    context = {'form': form}
    return render(request, 'election/create_election.html', context)


# homepage
def HomePage(request):
    context = {}
    return render(request, 'election/homepage.html', context)

# Add constituency


def AddConstituency(req):
    form = AddConstituencyForm()
    if req.method == "POST":
        form = AddConstituencyForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(req, 'election/add_consti.html', context)


# get constituency based on election
def get_constituencies(req):
    election_id = req.GET.get('election_id')
    constituencies = Constituency.objects.filter(election_id=election_id).all()
    # options = []
    # for item in constituencies:
    #     options.append({
    #         'id': item.id,
    #         'name': item.name
    #     })
    return render(req, 'election/consti_d_dlist.html', {'constituencies': constituencies})


# Add Candidate
def AddCandidate(req):
    form = AddCandidateForm()
    election = Election.objects.all()
    constituency = Constituency.objects.filter(election=election.first())
    if req.method == "POST":
        form = AddCandidateForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'elections': election,
        'constituencies': constituency
    }
    return render(req, 'election/add_cand.html', context)


def ShowCandidate(req):
    candidates = Candidates.objects.all()
    context = {
        'candi': candidates
    }
    return render(req, 'election/consti_details.html', context)


def AddVoter(req):
    form = AddVoterForm()
    if req.method == "POST":
        form = AddVoterForm(req.POST, req.FILES)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }
    return render(req, 'election/add_voter.html', context)
