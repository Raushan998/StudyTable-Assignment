from django.urls import path, include
from .views import index,get_view

urlpatterns = [
    path('',get_view,name='get_view'),
    path('index',index,name='index'),
]
