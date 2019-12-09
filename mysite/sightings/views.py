from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Squirrel
from .forms import SightingsForm

def display(request,*args,**kwargs):
    squirrels = Squirrel.objects.all()
    fields = ['Links by Squirrel ID', 'Date', 'longitude', 'Latitude']
    context={
        'squirrels':squirrels,
        'fields': fields,
    }  

    return render(request,'sightings/display.html',context)


def add(request):
    form =SightingsForm(request.POST)
    if form.is_valid():
        id=form['Unique_Squirrel_ID'].value()
        form.save()
        return redirect(f'/sightings/{id}')
    context={
       'form': form,
    }
    return render(request, 'sightings/add.html', context)


def stats(request):
   
    Total_Sightings=Squirrel.objects.all().count()
    Age_Adult=Squirrel.objects.filter(Age='Adult').count()
    Age_Juvenile=Squirrel.objects.filter(Age='Juvenile').count()
    Running=Squirrel.objects.filter(Running=True).count()
    Chasing=Squirrel.objects.filter(Chasing=True).count()
    Climbing=Squirrel.objects.filter(Climbing=True).count()
    Eating=Squirrel.objects.filter(Eating=True).count()
    Foraging=Squirrel.objects.filter(Foraging=True).count()
    context={
        'Total_Sightings': Total_Sightings,
        'Age_Adult': Age_Adult,
        'Age_Juvenile': Age_Juvenile,
        'Running': Running,
        'Chasing': Chasing,
        'Climbing': Climbing,
        'Eating': Eating,
        'Foraging': Foraging, 
    }
    return render(request,'sightings/stats.html',context)


def modify(request, squirrel_id):

    instance = get_object_or_404(Squirrel, Unique_Squirrel_ID=squirrel_id)
    form = SightingsForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect(f'/sightings/') 
    context ={
        'form':form,
        'squirrel_id':squirrel_id,
    }
    return render(request, 'sightings/modify.html', context)
