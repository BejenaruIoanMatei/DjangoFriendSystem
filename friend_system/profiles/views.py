from django.shortcuts import render
from .models import Profile, Relationship

# Create your views here.

def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request, 'profiles/myprofile.html', context)

def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_received(profile)
    
    context = {'qs':qs}
    
    return render(request, 'profiles/my_invites.html', context)