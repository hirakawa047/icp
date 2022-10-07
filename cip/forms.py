from django import forms

class ChannelIdForm(forms.Form):

    url_in = forms.CharField(label='channel_id', required=False)