from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import ChannelIdForm
from django.conf import settings
from django.http import JsonResponse


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
    print("OK")

        

    return render(request, 'cip/index.html',params)

def form(request):
    msg = request.POST['url_in']
    params = {'url_in':msg}

    print("OK")
    return render(request, 'cip/index.html',params)


def ContentsView(request):
    params = {
        'url_in' : 'Default value',
        'form' : ChannelIdForm(),
        }
    if (request.method=='POST'):
        params['url_in'] = request.POST.get('url_in')
    print(params)
    return render(request, 'cip/index.html', params)


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

def ajax_number(request):
    number1 = int(request.POST.get('number1'))
    number2 = int(request.POST.get('number2'))
    plus = number1 + number2
    minus = number1 - number2
    d = {
        'plus': plus,
        'minus': minus,
    }
    return JsonResponse(d)