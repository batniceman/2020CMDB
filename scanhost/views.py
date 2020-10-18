from django.shortcuts import render,HttpResponse

# Create your views here.

def scanhost(request):
    return HttpResponse('scan by self')