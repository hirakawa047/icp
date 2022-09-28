from django import forms

class getIDForm(forms.Form):

    title = forms.CharField(label='Input', required=False)