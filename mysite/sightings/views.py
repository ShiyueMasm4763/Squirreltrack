from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Squirrel
from .forms import SightingsForm

def display(request,*args,**kwargs):

    squirrels = Squirrel.objects.all()

    context={
        'squirrels':squirrels,
    }  

    return render(request,'sightings/display.html',context)


def add(request):
   
    if request.method == 'POST':
        Form =SightingsForm(request.POST)
        if Form.is_valid():
            Form.save()
            return redirect('sightings:display')
    else:
        Form = SightingsForm()
    context={
       'Form': Form,
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

    content1 = get_object_or_404(Squirrel, Unique_Squirrel_ID = squirrel_id)
    if request.method == "POST":
        content2 = SquirrelForm(request.POST, instance=content1)
        if content2.is_valid():
            content2.save()
            return redirect(f'/sightings/{squirrel_id}')
    context ={
        'form':content2,
        'sqid':squirrel_id,
    }
    return render(request, 'sightings/modify.html', context)
