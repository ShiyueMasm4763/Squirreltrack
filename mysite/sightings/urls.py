from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
        path('',views.display,name='sightings'),
        path('add/', views.add, name='add'),
        path('stats/',views.stats,name='stats'),
        path('<str:squirrel_id>',views.modify,name='modify'),
        ]
