from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from email.utils import formataddr
import socket
from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import Workwithus
from django.contrib.messages import get_messages

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def send_mail(name,mobile,email,company,field_of_work,desc,webap_v,app_v):
    print("Sending Mail")
    subject = "Hello "+name+"! Thank You For Reaching Out to Us."
    from_email = settings.DEFAULT_FROM_EMAIL
    html_content = render_to_string('NuvionMail.html', {'name':name,'mobile':mobile,'email':email,'company':company,'field_of_work':field_of_work,'desc':desc,'webap_v':webap_v,'app_v':app_v})
    
    email = EmailMultiAlternatives(
        subject,
        strip_tags(html_content),
        settings.DEFAULT_FROM_EMAIL,
        to=[email],
        cc=['shivam@nuviontech.com','harsh@nuviontech.com','om@nuviontech.com','harnish@nuviontech.com','jeel@nuviontech.com','samarth@nuviontech.com']
    )
    
    email.content_subtype = "html"
    email.attach_alternative(html_content, "text/html")
    
    email.send()
    print("Mail Sent Successfully")
from django.shortcuts import render
from django.http import HttpResponse
import requests

def work_with_us(request):
    if request.method == 'POST':
        form = Workwithus(request.POST)
        if form.is_valid():
            # form.save()

            import requests
            import gspread
            from datetime import datetime
            now = datetime.now()
            dt_string = now.strftime("%H:%M:%S %d/%m/%Y")
            from oauth2client.service_account import ServiceAccountCredentials
            scope = ['https://www.googleapis.com/auth/spreadsheets',
                    "https://www.googleapis.com/auth/drive"]
            credentials = ServiceAccountCredentials.from_json_keyfile_dict({
            "type": "service_account",
            "project_id": "sheets-360508",
            "private_key_id": "7710c2aa228331b17d0a6c9870303b2c15b6af77",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9j5ecBFG8lDam\nkCEthBaUKa0bZfEBOQtUa0Si9WpYMJJBCMqe3Fvf+K+x2FdYNBzPusIHHlxnRcG7\nJD5i5fdsrbGKJvD6f3ruxMKbLrcYkR4PgHthJAwIhtxfBs5xmfdFmuSpGnxDVWUY\nhyaYVOnlJSjwOP4QWssNWK9QaDVplPzpTY63Ir6M6IU9vORSILx4SGdTEcwIbkDP\nr+mHjs4UPsydleqnZ2Bsg7LTeSc5JaQdMFb6DKGFfFoH0j2X8HVwUu7gjoOX6hMq\ncjV+OVmy5ByIQhuigCBYS8zXbL/NyiKzm4nqlYjZLYqiAv881Mkf9axwDHjeIMkN\n5XlIWIbTAgMBAAECggEAQGPFvofTEekQlUyREIp1NvffJtbeYilz2UWkp2wQpws8\nqt2nIgY9KRuq5pDTvpDZFpDcNpnQDn5p+70oeeSewqpPi9uFcLmb0v5AEoFwTWaB\n3QcqIcmiUsUolxjTSFBh56FhObXW7vJTaF0ENatmVeFlAhCB8KE+pvZwerIjLo0I\n/4/ZW/Pd1T9VIFj4XU8+TgmCD7BTVd2nbpcEwjN/0/ng8YskI9rSQ6HFF+k3r16l\nbAsSQZa2sEWNfSCoM0+oTFfFTLa3QiAM0aKctFH+4gR28JX8LZ8W9iqEsXwBN+Cc\nt8yjAjapELYHv/BMyFXznCR7Eq33akpB2ZTs+a7LjQKBgQDlw0SKTU3uj8MZOpto\nDesTr/gqzqbv4HmU9GDEpBh3CmwqZLdunEEYXWLEJBSoJzD0H7HfuEhfIRarZYAC\nNTHb2D5MGL9z3+aAROIZAH7lPN1qcrt+rmapwGJ4GKjTDmAIH1eCRvGom8yrXM8l\nrVqDJvAvR+lzsLzMMLk1UsQ0vQKBgQDTNRcNsifpXJAVNesCTyZ6ec6rHm2YvK5g\nSh1l837fVqq/e+TabtRDsgzFVgH9MpOalk64tJjT3+3/DhJNMAVm93yjJJaI+pxb\n8Ao48S1RLJRZYAEcP3iTe7+9Az/WUx+9dilIp4N6Z+cxzciZ8VTXrxyrdVhcQXGr\ntm1mIpSKzwKBgCh7ZikkA7YjuFFKpTUJNsEKQSRxsrITD/jxsdcTvofC21oA0tz3\nRPThB1TdspIKDbMFnpZ3ZrD0KIVcZdh9vOIqUJehyKHG8lrpSBj1oGYNekmWG3jv\ni4EfN3pHhf9hygPEWevHSi7V/JK40Hqn94miI7GA7x4GJs2nTAqcIZvVAoGBAIz9\nos8Uv8nrbY+LN7+J4NDfoVPf8x+DzRAgSbG2M1qZ+0/qP+KFG5O5NwdAnAFPEvOe\nJRzuChteH/0kgpkeVmzfB0fM8+SrD1fcTKaocS0ACmQDT5pw0Gf7swpVMfc79DNA\nvtxuXrmGxPIdQi1pyc5ValkW845abaxIEo2cxfZHAoGAX8vNlfzgrvRxtiZx/62S\nv+pmptPBgl5DRUrT3OcWQ8c0Ko6scolZXVwEjAnCBjvXj3qSubjsV3DIJEtGlerU\nvSjL91yD1bXhHeVwJtDcj0qeGEkcPz4ZSim8F7jInby4xsdkMgnOEhsANX8wbQzX\nlNv1du/F5pzg7diwZVWRJGA=\n-----END PRIVATE KEY-----\n",
            "client_email": "shivam-27@sheets-360508.iam.gserviceaccount.com",
            "client_id": "104455111396914151163",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/shivam-27%40sheets-360508.iam.gserviceaccount.com"
            }
            , scope)
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            company = request.POST.get('company')
            field_of_work = request.POST.get('field_of_work')
            desc = request.POST.get('desc')
            webap = 'webap' in request.POST
            print(webap)
            if webap==True:
                webap_v="Yes"
            else:
                webap_v="No"
            app = 'app' in request.POST
            if app==True:
                app_v="Yes"
            else:
                app_v="No"
            client = gspread.authorize(credentials)
            sheet = client.open("Work_With_Us_Data")
            sheet_instance=sheet.get_worksheet(0)
            records_data = sheet_instance.get_all_records()
            lenr=len(records_data)
            i=[lenr+1,name,mobile,email,company,field_of_work,webap,app,desc,dt_string]
            sheet_instance.insert_row(i,lenr+2)
            send_mail(name,mobile,email,company,field_of_work,desc,webap_v,app_v)
            messages.success(request, 'Your form has been submitted successfully! Our Team Will Contact You Soon!')
            return redirect('/workwithus')
    else:
        form = Workwithus()
    stored_messages = get_messages(request)
    return render(request, 'index.html', {'form': form, 'messages': stored_messages})
