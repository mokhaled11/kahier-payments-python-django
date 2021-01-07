from django.shortcuts import render
 
from . import backend , config

import urllib.parse 
import time


# Create your views here.

def index(request): 
     
    configDict = config.config["live-test"]
 
    order= {
        "amount": 20.00,
        "currency": "EGP",
        "merchantOrderId":round(time.time()) 
     
    }
    order['mid']=configDict["mid"]
    order["secret"]=configDict["iframeSecret"]
    order["baseUrl"]=configDict["baseUrl"]


    hash=backend.generateKashierOrderHash(order)
    
    order["hash"]=hash
    order["secret"]=configDict["HPPSecret"]
    
    phash=backend.generateKashierOrderHash(order)
    callbackUrl= urllib.parse.quote('http://localhost:8000/hppCallback')
    order["callbackUrl"]=callbackUrl
    order["phash"]=phash
    hppUrl = '{baseUrl}/payment?mid={mid}&orderId={merchantOrderId}&amount={amount}&currency={currency}&hash={phash}&merchantRedirect={callbackUrl}'.format(**order)
    
    context = {
        "order":order,
        "hppUrl":hppUrl,
    }
    return render(request, "payment/index.html" , context)



def callback(request):
    
    configDict = config.config["live-test"]
    secret = configDict["iframeSecret"]

    result = backend.validateSignature(request.GET,secret)

    return render(request, f"payment/{result}.html" )
   



def hppCallback(request):
    
    configDict = config.config["live-test"]
    secret = configDict["HPPSecret"]

    result = backend.validateSignature(request.GET,secret)

    print(result)
    return render(request, f"payment/{result}.html" )