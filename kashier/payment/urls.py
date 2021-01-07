from django.urls import path
from . import views 

app_name='payment'

urlpatterns = [
    path("",views.index,name="index"),
    path("callback/",views.callback,name="callback"),
    path("hppCallback/",views.hppCallback,name="hppCallback")
    
]