from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. And this comment is to check
def index(request) :
    return HttpResponse('Main Writer Module Page')

def docList(request, user_name) :
    return HttpResponse("List of notes for user: "+user_name)

def docRead(request, doc_id) :
    return HttpResponse("Showing document: " + doc_id)