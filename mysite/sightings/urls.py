from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
        path('',views.display,name='sightings'),
        ]
