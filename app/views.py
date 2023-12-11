from django.shortcuts import render
from django.http import HttpResponse



def Twinkle(request):
    return HttpResponse('<h1>Hate you</h1>')



def Akankshya(request):
    return HttpResponse('<marquee>Love You</marquee>')

# Create your views here.
