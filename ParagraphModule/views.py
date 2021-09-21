from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Paragraph, ParagraphLinks
from .forms import ParagraphEditForm

# Create your views here.
def index(request) :
    context = {
    }
    return render(request, 'ParagraphModule/index.html', context)

def paragraphList(request, user_name) :
    par_list = Paragraph.objects.all()
    context = {
        'par_list' : par_list,
        'page_title' : "Paragraphs"
    }
    return render(request, 'ParagraphModule/par_list.html', context)

def paragraphEdit(request, user_name) :
    submitted = False
    if request.method == 'POST':
        form = ParagraphEditForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('paragraph/addParagraph?submitted=True')
    else:
        form = ParagraphEditForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'ParagraphModule/par_add.html', 
            {'form' : form, 'submitted' : submitted})

