from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader

from .models import MainTextBody

# Create your views here. And this comment is to check
def index(request) :
    doc_list = MainTextBody.objects.order_by('-last_update_date')
    print (doc_list)
    context = {
        'doc_list' : doc_list
    }
    return render(request, 'WriterModule/index.html', context)

def docInfo(request, doc_id) :
    doc_list = MainTextBody.objects.all()
    doc_data = []
    for d in doc_list :
        if d.text_id == doc_id :
            doc_data = d.getTextMetadata()
            break
    return HttpResponse(str(doc_data))

def docList(request, user_name) :
    return HttpResponse("List of notes for user: " + user_name)

def docRead(request, doc_id) :
    return HttpResponse("Showing document: " + str(doc_id))