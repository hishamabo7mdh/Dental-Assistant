from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile, name='profile'),
    #path('visit/',views.visit,name="visit"),
    path('viewVisits/<str:pk>',views.viewVisits,name="viewVisits"),
    path('',views.home,name='home'),
    path('create_profile/',views.addProfileToDB,name="create_profile"),
    path('update_profile/<str:pk>/',views.updateProfile,name="update_profile"),
    path('delete_profile/<str:pk>/',views.deleteProfile,name="delete_profile"),
 
]
