from django.contrib import admin
from .models import Trip, Category, Expense, TravelCompanion, ExpenseSplit
admin.site.register(Trip)
admin.site.register(Category)
admin.site.register(Expense)            
admin.site.register(TravelCompanion)
admin.site.register(ExpenseSplit)

# Register your models here.
