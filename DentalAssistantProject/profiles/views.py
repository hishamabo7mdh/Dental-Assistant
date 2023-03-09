
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Profile,Visits
from .forms import *
from .filters import ProfileFilter
# Create your views here.

def addProfileToDB(request):
    form=ProfileForm()
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully')
            return redirect('/profile/')
        else:
            messages.success(request, 'not successfully')

    context={'form':form  }    
        
        
    return render(request,'profile/profile_form.html',context) 

#update profile
def updateProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    form=ProfileForm(instance=profile)
    if request.method=='POST':
        form=ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    context={'form':form}
    return render(request,'profile/profile_form.html',context)

#delete profile
def deleteProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    if request.method=="POST":
        profile.delete()
        return redirect('/profile/')
    context={'profile':profile}
    return render(request,'profile/delete.html',context)
     
    

     
def addVisitToDB(request):
    if request.method == 'POST':
        data=Visits(image=request.POST['image'],description=request.POST['description'],dateCreated=request.POST['dateCreated'],profileId=request.POST['profileId'])
        data.save()
        messages.success(request, '')
    else:
        messages.error(request,'')
        
#visit
#def visit(request):
#    context={}
#    return render(request,'profile/visit.html',context)


#view visits
def viewVisits(request,pk):
    pro=Profile.objects.get(id=pk)
    visitAll=Visits.objects.all()
    visit=visitAll.filter(profileID=pro)
    context={'visit':visit}
    return render(request,'profile/visit.html',context)
    
        
def profile(request):
    
    profile=Profile.objects.all()
    #search------------
    searchFilter=ProfileFilter(request.GET , queryset=profile)
    profile=searchFilter.qs 
    context={'profile':profile , 'search':searchFilter} 
    return render(request,'profile/profile.html',context)



#home page***********************************************************************************
def home(request):
    return render(request,'profile/home.html')


