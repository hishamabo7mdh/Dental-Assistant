from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile, name='profile'),
    path('',views.home,name='home'),
    path('create_profile/',views.addProfileToDB,name="create_profile"),
 
]
