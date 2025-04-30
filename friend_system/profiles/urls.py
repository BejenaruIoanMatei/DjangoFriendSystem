from django.urls import path
from .views import my_profile, invites_received_view

urlpatterns = [
    path('myprofile/', my_profile, name='my-profile-view'),
    path('my-invites/', invites_received_view, name='my-invites-view'),
]
