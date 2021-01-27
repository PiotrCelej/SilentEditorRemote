from django import template
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader
from django.urls import reverse

from .models import MainTextBody

# Create your views here. And this comment is to check
def index(request) :
    context = {
    }
    return render(request, 'WriterModule/index.html', context)

def docInfo(request, doc_id) :
    doc_list = MainTextBody.objects.filter(text_id=doc_id)
    doc_data = doc_list[0]
    return HttpResponse(str(doc_data))

def docList(request, user_name) :
    doc_list = MainTextBody.objects.filter(author=user_name).order_by('-last_update_date')
    context = {
        'doc_list' : doc_list,
        'page_title' : "Writer Module Doc List"
    }
    return render(request, 'WriterModule/doc_list.html', context)

def docRead(request, doc_id) :
    doc_list = MainTextBody.objects.filter(text_id=doc_id)
    doc_data = doc_list[0]
    context = {
        'doc_name' : doc_data.name,
        'doc_date' : doc_data.last_update_date,
        'doc_text' : doc_data.body_text
    }
    return render(request, 'WriterModule/doc_view.html', context)

def docWrite(request, doc_id) :
    doc_list = MainTextBody.objects.filter(text_id = doc_id)
    doc_data = doc_list[0]

    try :
        doc_data.body_text = request.POST['doc_text']
    except (KeyError, MainTextBody.DoesNotExist) :
        return render(
            request, 
            'WriterModule/doc_write.html',
            {
                'doc' : doc_data,
                'message' : "Your document has not been saved"
            }
        )
    else :
        doc_data.save()
        return HttpResponseRedirect(reverse('docWrite', args=(doc_data.text_id,)))
