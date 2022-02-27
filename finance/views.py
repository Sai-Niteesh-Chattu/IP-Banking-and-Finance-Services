from datetime import date

from django.contrib import messages
from django.shortcuts import render, redirect
from finance.forms import LoanForm
from finance.models import *
# Create your views here.

def loanview(request):
    print("its coming")
    try:
        query = Loans.objects.filter(username = request.session['username'])
    except Loans.DoesNotExist:
        query = None
    context = {'object_list' : query}
    return render(request,'loans.html',context)

def loanform(request):

    if request.method == "POST":
        s=Loans()
        s.fname=request.POST.get('fname')
        s.lname = request.POST.get('lname')
        s.mail = request.POST.get('mail')
        s.desired_loan_amount = int(request.POST.get('loanamt'))
        s.annual_income =int(request.POST.get('income'))
        s.loan_required_for = request.POST.get('type')
        s.loan_duration=int(request.POST.get('time'))
        s.phonenumber=request.POST.get('phno')
        s.occupation=request.POST.get('job')

        if s.loan_required_for == "Home Loan":
            s.intrest=7.0
            s.max_loan=1500000
        elif s.loan_required_for == "Gold Loan":
            s.intrest = 6.5
            s.max_loan = 500000
        elif s.loan_required_for == "Education Loan":
            s.intrest = 6.8
            s.max_loan = 1000000
        else :
            s.intrest = 6.2
            s.max_loan = 800000

        #form= LoanForm(s)
        print("whats happening")
        #for field in form:
        #    print("Field Error:", field.name, field.errors)
        #if form.is_valid():
        #    instance = form.save(commit = False)
        instance=s
        instance.username = request.session['username']
        instance.loan_date = date.today()
            #loa = LoanInfo.objects.get(loan=instance.loan_required_for)
            #instance.intrest = loa.loan_intrest
        if instance.desired_loan_amount <= instance.max_loan:
            a = ((instance.intrest * instance.desired_loan_amount) / 100) * instance.loan_duration
            b = a + instance.desired_loan_amount
            c = b / instance.loan_duration
            d = 0.6 * instance.annual_income
            if c <= d:
                    instance.status = 'approved'
                    instance.save()
                    #messages.success(request,f"your loan is sactioned")
                    return redirect('finance:loans')
        instance.status = "disapproved"
        instance.save()
        #messages.error(request,f"loan is not sactioned for your requirments")
        return redirect("finance:loans")

        print("whats happening")
        form = LoanForm()
        #context = {'form' : form }

    return render(request,"loanform.html")#,context)