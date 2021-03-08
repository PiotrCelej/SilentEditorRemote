from django import forms
from django.forms.fields import CharField
from .models import MainTextBody
from django_summernote.fields import SummernoteTextField

class DocEditForm(forms.ModelForm) :
    class Meta :
        model = MainTextBody
        #fields = '__all__'
        fields = ['name','body_text']
        name = CharField()
        body_text = SummernoteTextField()
