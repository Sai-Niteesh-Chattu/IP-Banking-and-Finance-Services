from django.db import models

from .constants import TRANSACTION_TYPE_CHOICES

class Transactions(models.Model):
    user_account_number = models.CharField(max_length=15,blank=False)
    dest_account_number = models.CharField(max_length=15, blank=False)
    ifsc_no = models.CharField(max_length = 6, blank = False , default = "000000")
    bank = models.CharField(max_length=10, blank=False, default="ssss")
    branch = models.CharField(max_length=18, blank=False, default="dddd")
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        null=True,
        blank = True
    )
    transaction_type = models.CharField(
        choices=TRANSACTION_TYPE_CHOICES,
        max_length=20,
        null=True,
        blank = True
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']


class Status (models.Model):
    account_no = models.CharField(max_length = 15, default = None,blank=False)
    balance = models.IntegerField(default = None,blank=False)
    username = models.CharField(max_length = 150, default = None,blank=False)

    @property
    def amt(self):
        return self.balance > 0



class Employee(models.Model):
    username = models.CharField(max_length=50,unique=True,null = False,blank = False)
    password = models.CharField(null = False,blank = False,max_length=20)