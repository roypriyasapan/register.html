from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.
def register(request):
    return render(request, 'register.html')

def registerdata(request):
    # return render(request, 'register.html')
    print(request.method)
    print(request.POST)

