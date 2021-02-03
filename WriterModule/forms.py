from django import forms

class DocEditForm(forms.Form) :
    body_text = forms.CharField(label='Text Area should be here')