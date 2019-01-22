from django.db import models

# Create your models here.

class Member(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=10)
    user_phone = models.CharField(max_length=20)
    user_sale = models.CharField(max_length=40)
    user_buy = models.CharField(max_length=40)
    time = models.DateTimeField(auto_now_add=True)
