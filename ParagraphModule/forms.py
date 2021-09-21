from django import forms
from .models import Paragraph, Character
from django.forms.fields import CharField, BooleanField

class ParagraphEditForm(forms.ModelForm) :
    class Meta:
        model = Paragraph
        fields = '__all__'

class CharacterEditForm(forms.ModelForm) :
    class Meta:
        model = Character
        fields = '__all__'