from django.shortcuts import render

def hello(request):
    return render(request,'hello/hello.html')
# Create your views here.

def goodbye(request):
    return render(request,'hello/goodbye.html')
