
from django.contrib import admin
from django.urls import path,include

#mapping to the new app url file
urlpatterns = [
    path('ContactsApp/',include('ContactsApp.urls')),
    path('admin/', admin.site.urls),
]
