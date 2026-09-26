from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('Tripform/', Tripform, name='Tripform'),
    path('Categoryform/', Categoryform, name='Categoryform'),
    path('Expenseform/', Expenseform, name='Expenseform'),
    path('Travelcompanionform/', Travelcompanionform, name='Travelcompanionform'),
    path('ExpenseSplitform/', ExpenseSplitform,  name='ExpenseSplitform'),

]
