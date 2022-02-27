import datetime

from django import forms
from django.conf import settings

from .models import  Transactions
from . import models

class TransactionDateRangeForm(forms.Form):
    daterange = forms.CharField(required=False)
    def clean_daterange(self):
        daterange = self.cleaned_data.get("daterange")
        try:
            daterange = daterange.split(' - ')

            if len(daterange) == 2:
                for date in daterange:
                    datetime.datetime.strptime(date, '%Y-%m-%d')
                return daterange
            else:
                raise forms.ValidationError("Please select a date range.")
        except (ValueError, AttributeError):
            raise forms.ValidationError("Invalid date range")

class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            "ifsc_no",
            "dest_account_number",
            "amount"

        ]