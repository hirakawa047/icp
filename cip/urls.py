from django.urls import path
from .views import ChannelIdView

app_name = "cip"
urlpatterns = [
    path('', ChannelIdView.as_view(), name='index'),
]