from django.shortcuts import render
from .models import Paragraph, ParagraphLinks

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
