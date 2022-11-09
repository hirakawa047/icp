from django.urls import path
from .views import ChannelIdView
from .views import ContentsView, ajax_number

#app_name = "cip"
urlpatterns = [
    #path('', ChannelIdView.as_view(), name='index'),
    path('', ContentsView, name='ContentsView'),
    path('ajax-number/', ajax_number, name='ajax_number'),
]