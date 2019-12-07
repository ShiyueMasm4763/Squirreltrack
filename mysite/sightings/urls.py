from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
        path('',views.display,name='sightings'),
        path('<str:sq_id>',views.modify,name='modify'),
        path('add/', views.add.as_view(), name='add'),
        path('stats/',views.stats,name='stats'),
        ]
