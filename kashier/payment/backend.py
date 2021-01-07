

#Copy and paste this code in your Backend
import hmac
import hashlib
import binascii

def generateKashierOrderHash(order):
    mid = "MID-3552-454"; 
    amount = order['amount'] 
    currency = order['currency']
    orderId = order['merchantOrderId']
    path = '/?payment={}.{}.{}.{}'.format( mid, orderId, amount, currency )
    path = bytes(path, 'utf-8')
    secret = order["secret"]

    secret = bytes(secret, 'utf-8')
    return hmac.new(secret, path, hashlib.sha256).hexdigest()

   
   
def validateSignature(request , secret):
    queryString = ""
    for key in request: 
       if key == "signature" or key =="mode" :
         continue
       queryString = queryString + "&" + f'{key}=' + request[key]


    queryString = queryString[1:] 
    secret = bytes(secret, 'utf-8')
    queryString  = queryString.encode()
    signature = hmac.new(secret, queryString, hashlib.sha256).hexdigest()

    if signature == request.get("signature"):
        return "success"    
    else :
        return "failure"
         