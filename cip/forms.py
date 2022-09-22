from django import forms

class getIDForm(forms.Form):

    id = forms.CharField(label='Input', required=True)