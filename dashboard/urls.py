from django.urls import path
from .views import *
urlpatterns = [
    path('',BLife_view,name = 'home'),
]