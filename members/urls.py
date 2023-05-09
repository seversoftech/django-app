from django.urls import path
from . import views

urlpattern=[
    path('members/', views.members,name=members),
]