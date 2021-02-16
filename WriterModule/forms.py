from django import forms
from .models import MainTextBody

class DocEditForm(forms.ModelForm) :
    class Meta :
        model = MainTextBody
        fields = '__all__'
