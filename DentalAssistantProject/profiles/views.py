
from pyexpat.errors import messages
from django.shortcuts import render
from .models import Profile,Visits
# Create your views here.
def addProfileToDB(request):
    if request.method == 'POST':
        data=Profile(name=request.POST['name'],gender=request.POST['gender'])
        data.save()
        messages.success(request, '')
    else:
        messages.error(request,'')
def addVisitToDB(request):
    if request.method == 'POST':
        data=Visits(image=request.POST['image'],description=request.POST['description'],dateCreated=request.POST['dateCreated'],profileId=request.POST['profileId'])
        data.save()
        messages.success(request, '')
    else:
        messages.error(request,'')
def profile(request):
    return render(request,'profile/profile.html')