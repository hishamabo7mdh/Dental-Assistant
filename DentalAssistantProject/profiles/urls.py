from django.urls import path
from . import views

urlpatterns = [
    path('viewVisits/<str:pk>',views.viewVisits,name="viewVisits"),
    path('',views.profile,name='home'),
    path('profile/',views.ppp,name='profile'),
    path('create_profile/',views.addProfileToDB,name="create_profile"),
    path('update_profile/<str:pk>/',views.updateProfile,name="update_profile"),
    path('delete_profile/<str:pk>/',views.deleteProfile,name="delete_profile"),
 
]
