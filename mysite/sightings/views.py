from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Squirrel


def display(request,*args,**kwargs):

    list1 = Squirrel.objects.all()
    list2 = ['Unique_Squirrel_ID','Location','Date']

    context={
        'squirrels':list1,
        'fields':list2,
    }    

    return render(request,'sightings/sightings_display.html',context)


class add(CreateView):

    model = Squirrel
    fields = '__all__'
    success_url = reverse_lazy('sightings:sightings')


def stats(request):
    
    list3 = Squirrel.objects.all()
    context={
        'squirrels':list3,        
    }
    return render(request,'sightings/sightings_stats.html',context)


def modify(request, sq_id):

    content1 = get_object_or_404(Squirrel, Unique_Squirrel_ID = sq_id)
    content2 = SightingsForm(request.POST or None,instance = content1)
    if content2.is_valid():
        content2.save()
        return redirect(f'/sightings/{sq_id}')
    context ={
        'form':content2,
        'sqid':sq_id,
    }
    return render(request, 'sightings/modify.html', context)
