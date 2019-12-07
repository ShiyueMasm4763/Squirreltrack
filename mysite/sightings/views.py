from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .forms import SightingsForm
from .models import Squirrel



def display(request,*args,**kwargs):

    list1 = Squirrel.objects.all()
    list2 = ['Unique_Squirrel_ID','Location','Date']

    context={
        'squirrels':list1,
        'fields':list2,
    }    

    return render(request,'sightings/sightings_list.html',context)

