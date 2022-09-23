from django.shortcuts import render
from django.template import loader
from .forms import getIDForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        f = getIDForm(request.POST)
    else:
        f = getIDForm()
    print(f)
    return render(request,'cip/index.html', {'form1': f})