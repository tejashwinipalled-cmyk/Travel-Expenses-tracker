from django.shortcuts import render

# Create your views here.
def Tripform(request):
    return render(request,'core/Tripform.html')

def Categoryform(request):
    return render(request ,'core/Categoryform.html')

def Expenseform(request):
    return render(request ,'core/Expenseform.html')

def Travelcompanionform(request):
    return render(request ,'core/Travelcompanionform.html')

def ExpenseSplitform(request):
    return render(request ,'core/ExpenseSplitform.html')
