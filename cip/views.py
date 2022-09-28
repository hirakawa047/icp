from django.shortcuts import render,redirect

from django.views import View
from .models import Topic

class IndexView(View):

    def get(self, request, *args, **kwargs):

        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"cip/index.html",context)

    def post(self, request, *args, **kwargs):

        posted  = Topic( name = request.POST["name"] )
        posted.save()

        return redirect("cip:index")

index   = IndexView.as_view()