from django.db import models

# Create your models here.

class Loans(models.Model):
    loan_choices  = (
          ('HomeLoan','HomeLoan'),
          ('EducationLoan','EducationLoan'),
          ('GoldLoan','GoldLoan'),
          ('CarLoan','CarLoan')
      )
    approved_choices = (
        ('approved','approved'),
        ('disapproved','disapproved'),
        ('pending','pending')
    )
    fname=models.CharField(max_length=20,blank=False)
    lname=models.CharField(max_length=20,blank=False)
    username=models.CharField(max_length=50,blank=False)
    mail = models.EmailField (null= False,blank=False,max_length = 30)
    desired_loan_amount = models.IntegerField(null = False)
    annual_income = models.IntegerField(null = False)
    loan_required_for = models.CharField(max_length = 50,choices = loan_choices)
    loan_duration= models.IntegerField(null=False)
    phonenumber = models.BigIntegerField(blank = False,null = False,max_length=10)
    occupation = models.CharField(null = False,max_length=50,blank = False)
    status = models.CharField(max_length=50, choices = approved_choices)
    loan_date = models.DateField(null=True, blank=True)
    intrest = models.DecimalField(decimal_places=2,max_digits=6,null = True, blank=True)
    max_loan=models.IntegerField(blank=False)