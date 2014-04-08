from django.contrib.auth.models import User
from django.db import models

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    country = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=10)
    
    