from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('create/',views.createandshow,name='createandshow'),
    path('delete/',views.delete,name='deletedata'),
    path('update/',views.update,name='updatedata'),



]