from django import template
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import context, loader
from django.urls import reverse
from collections import Counter

from .models import MainTextBody
from .forms import DocEditForm

#forms view goes here
def getTextBody(request, doc_id) :
    print (doc_id)
    text = MainTextBody.objects.filter(text_id = doc_id)
    context = {
        'doc_name' : "text.name"
    }
    if request.method == 'POST' :
        form = DocEditForm(request.POST)
        if form.is_valid() :
            doc_text = form.cleaned_data['body_text']
            try :
                text.body_text = doc_text
                text.save()
            except doc_text.DoesNotExist() :
                raise Http404('Text does not exist')
            return HttpResponseRedirect(f'doc_write.html', {
                'form' : form,
                'doc_name' : text.name,
                'wr_message' : "Document saved",
            })
    else :
        form = DocEditForm()
        context = {
            'form' : form,
#            'doc_name' : text.name,
            'wr_message' : "New document"
        }
    return render(request, 'doc_write.html', context)

# Create your views here. And this comment is to check
def index(request) :
    context = {
    }
    return render(request, 'WriterModule/index.html', context)

def docInfo(request, doc_id) :
    doc_data = get_object_or_404(MainTextBody, text_id = doc_id)
    return HttpResponse(str(doc_data))

def docList(request, user_name) :
    doc_list = MainTextBody.objects.filter(author=user_name).order_by('-last_update_date')
    context = {
        'doc_list' : doc_list,
        'page_title' : "Writer Module Doc List"
    }
    return render(request, 'WriterModule/doc_list.html', context)

def docRead(request, doc_id) :
    doc_data = get_object_or_404(MainTextBody, text_id = doc_id)
    no_lines = Counter(doc_data.body_text)
    rows = no_lines['\n']+2
    context = {
        'doc' : doc_data,
        'doc_rows' : rows
    }
    return render(request, 'WriterModule/doc_view.html', context)

def docWrite(request, doc_id) :
    doc_data = get_object_or_404(MainTextBody, text_id = doc_id)
    
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
