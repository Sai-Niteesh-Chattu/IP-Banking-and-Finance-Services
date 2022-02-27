from django.db import models

class User(models.Model):
    accountnumber=models.CharField(max_length=15,blank=False,unique=True)
    username = models.CharField(max_length=100, blank=False)
    email=models.EmailField(max_length=30,blank=False)
    password=models.CharField(max_length=20,blank=False)
    accounttype=models.CharField(max_length=20,blank=False,default="savings account")
    ifsc_no = models.CharField(max_length = 6, blank = False , default = "000000")
    bank = models.CharField(max_length = 50 , blank = False , default = "aaaaaa")
    branch = models.CharField(max_length = 50 , blank = False , default = "aaaaa")

    class Meta:
        db_table="user_table"


class Student(models.Model):
    SID=models.IntegerField(blank=False,default = 0)
    name=models.CharField(max_length=30,blank=False)
    gender = models.CharField(max_length=10,blank=False)
    department=models.CharField(max_length=20,blank=False)
    year=models.IntegerField(blank=False)
    semester=models.IntegerField()
    mailid=models.EmailField(max_length=10)
    mobile=models.IntegerField(max_length=10)