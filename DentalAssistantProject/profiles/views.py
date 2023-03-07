
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import Profile,Visits
from .forms import *
from .filters import ProfileFilter
# Create your views here.




def addProfileToDB(request):
    # if request.method == 'POST':
    #     data=Profile(name=request.POST['name'],gender=request.POST['gender'])
    #     data.save()
    #     messages.success(request, '')
    # else:
    #     messages.error(request,'')
    
    form=ProfileForm()
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    
        
    context={'form':form}    
        
        
    return render(request,'profile/profile_form.html',context) 

     
def addVisitToDB(request):
    if request.method == 'POST':
        data=Visits(image=request.POST['image'],description=request.POST['description'],dateCreated=request.POST['dateCreated'],profileId=request.POST['profileId'])
        data.save()
        messages.success(request, '')
    else:
        messages.error(request,'')
def profile(request):
    profile=Profile.objects.all()
    #filter
    context={'profile':profile}
    
    return render(request,'profile/profile.html',context)


#home page***********************************************************************************
def home(request):
    return render(request,'profile/home.html')


