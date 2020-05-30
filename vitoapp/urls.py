from django.shortcuts import render
from django.urls import path
from vitoapp import views
#Add your views here

app_name = 'vito'

urlpatterns=[
    path('',views.index,name='index'),
    path('add/vito/',views.add_vito,name = 'add_vito'),
    path('vitos/',views.BusListView.as_view(extra_context={'title':'Vitos'}),name='vitos'),
    path('vito/<int:pk>/details/',views.BusDetailView.as_view(extra_context={'title':'Vito Deatils'}),name='vito_detail')
]