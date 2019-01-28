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

    def __str__(self):
        return self.user_id

class Casend(models.Model):
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    date = models.CharField(max_length=30)
    price = models.CharField(max_length=10)
    ele = models.CharField(max_length=10)
    time2 = models.DateTimeField(auto_now_add=True)

class Bsend(models.Model):
    user_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    address2 = models.CharField(max_length=100)
    date2 = models.CharField(max_length=30)
    price2 = models.CharField(max_length=10)
    ele2 = models.CharField(max_length=10)
    time2 = models.DateTimeField(auto_now_add=True)
