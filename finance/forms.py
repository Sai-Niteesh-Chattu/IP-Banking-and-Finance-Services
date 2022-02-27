from django.forms import ModelForm
from .models import Loans

class LoanForm(ModelForm):

    class Meta:
        model=Loans
        fields = [
            "fname",
            "lname",
            "mail",
            "desired_loan_amount",
            "annual_income",
            "loan_required_for",
            "loan_duration",
            "phonenumber",
            "occupation",
            "intrest",
            "max_loan"
        ]