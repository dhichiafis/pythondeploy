from django.shortcuts import render

def hello(request):
    return render(request,'hello/hello.html')
# Create your views here.

def goobye(request):
    return render(request,'hello/goodbye.html')
