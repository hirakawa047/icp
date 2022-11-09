from django import forms

class ChannelIdForm(forms.Form):

    url_in = forms.CharField(label='url_in', required=False)