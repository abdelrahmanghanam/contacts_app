from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='index'),
path('get_contact_details',views.get_contact_details,name='get_contact_details'),
path('add_new_number',views.add_new_number,name='add_new_number'),
path('create_new_contact',views.create_new_contact,name='create_new_contact'),
]
