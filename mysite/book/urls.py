from django.urls import path
from django.views.generic import *
from .models import Book

app_name = 'book'

urlpatterns = [
    path('', ListView.as_view(model=Book), name='list'),
    path('detail/<pk>', DetailView.as_view(model=Book), name='detail'),
]
