from django.shortcuts import render, redirect
from election.models import Election
from django.conf import settings
import cv2
import os 
# Create your views here.


def startElection(req):
    allElections = Election.objects.all().values()
    # for election in allElections:
    #     print(election)
    context = {
        'elections': allElections
    }
    return render(req, 'startElection/elections.html', context)


def capture_image(request):
    cap = cv2.VideoCapture(0)
    success, frame = cap.read()
    if success:
        filename = os.path.join(settings.MEDIA_ROOT, 'captured_image.jpg')
        cv2.imwrite(filename, frame)
        cap.release()
        return redirect('capture_image_success')
    else:
        cap.release()
        return render(request, 'capture_image_error.html')


# def election_start(request):