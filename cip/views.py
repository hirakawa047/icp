from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ChannelIdForm





#class IndexView(View):



def index(request):
    params = {
            'url_in':'empty'
        }
    #return render(request,'cip/index.html',params)

#index   = IndexView.as_view()
    if (request.method =='POST'):
        params = {
        'url_in' : request.POST['url_in']
        }
    return render(request, 'cip/index/html',params)

def form(request):
    msg = request.POST['url_in']
    params = {'url_in':msg}
    return render(request, 'cip/index.html',params)

def ContentsView(request):
    return render(request, 'cip/contents.html')


class ChannelIdView(TemplateView):

    def __init__(self):
        self.channel_id = {
            'channel_id' : ChannelIdForm()
        }
    
    def get(self,request):
        return render(request, 'cip/index.html',self.channel_id)
    
    def post(self,request):
        self.channel_id['idForm'] = ChannelIdForm(request.POST)
        return render(request, 'cip/index.html',self.channel_id)