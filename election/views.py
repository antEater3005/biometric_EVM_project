from django.shortcuts import render
from django.http import HttpResponse
from .forms import ElectionForm
# Create your views here.


def CreateElection(request):
    form = ElectionForm()

    if request.method == 'POST':
        form = ElectionForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'election/create_election.html', context)


# homepage
def HomePage(request):
    context = {}
    return render(request, 'election/homepage.html', context)



