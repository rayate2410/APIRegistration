from django.http import *
from django.views.decorators.csrf import csrf_exempt
import os
from django.contrib.auth.models import User
from APIBasedProject.models import UserInfo
import json
from django.core.mail import send_mail

@csrf_exempt
def registerUser(request):
    
    email = request.POST['email']
    password = request.POST['password']
    country = request.POST['country']
    mobile_no = request.POST['mobile_no']
    response_data = {}
    
    try:
        user = User.objects.create_user(email, email, password)
        user.is_active=False
        
        
        user_info = UserInfo(user = user,country = country, mobile_no = mobile_no)
        user_info.save()
        
        send_mail
        
        response_data['message'] = "registration successful"
        response_data['stat'] = "ok"
    except:
        response_data['message'] = "registration failed"
        response_data['stat'] = "failed"
      
    return HttpResponse(json.dumps(response_data,indent=4), content_type="application/json")
    
