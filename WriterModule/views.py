from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. And this comment is to check
def index(request) :
    return HttpResponse('Main Writer Module Page')