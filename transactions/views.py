from django.db.models import Q, Count, Sum
from django.forms import forms
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from demoapp.models import User
from finance.models import Loans
from .forms import MoneyTransferForm,TransactionDateRangeForm
from .constants import *
from .models import *
from transactions import *
from django.contrib import messages
from .utils import get_plot


# Create your views here.



def transfer(request):
    if request.method == "POST":

        form = forms.MoneyTransferForm(request.POST)

        if form.is_valid():
            print(form)

            try:
                userr = User.objects.get(ifsc_no=request.POST.get('ifsc_no'))
            except User.DoesNotExist:
                userr = None


            curr1_user = Status.objects.get(username=request.session['username'])
            try:
                da=request.POST.get("dest_account_number")
                dest_user = Status.objects.get(account_no=da)
            except Status.DoesNotExist:
                dest_user = None
            if userr == None:
                messages.error(request, "We are not connected with your bank")
                form = forms.MoneyTransferForm()
                context = {'form': form}
                return render(request, "transfer.html", context)
            if int(request.POST.get('amount')) > curr1_user.balance:
                messages.error(request,'your transfer amount need to be beyond your balance')
                form = forms.MoneyTransferForm()
                context = {'form': form}
                return render(request,"transfer.html",context)
            if int(request.POST.get('amount'))  < 0:
                messages.error(request,"you need to transfer amount greater than 0")
                form = forms.MoneyTransferForm()
                context = {'form': form}
                return render(request,"transfer.html",context)
            if dest_user == None:
                messages.error(request, "you need to transfer to the correct account number")
                form = forms.MoneyTransferForm()
                context = {'form': form}
                return render(request, "transfer.html",context)



            form.save()
           # usee = UserBankAccount.objects.get(user = request.user)

            curr_user = Transactions.objects.last()

            dest_account_number = curr_user.dest_account_number

            print(curr_user)
            print(curr_user.dest_account_number)


            transfer_amount = curr_user.amount


            a = User.objects.get(username=request.session['username'])
            curr_user.user_account_number = a.accountnumber



            print(curr1_user)
            print(transfer_amount)
            curr1_user.balance = curr1_user.balance - transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount

            curr_user. balance_after_transaction =  curr1_user.balance
            curr_user.transaction_type = Transfered_to
            print(curr_user.balance_after_transaction)
            #usee.balance = curr1_user.balance
            curr_user.bank = userr.bank
            curr_user.branch = userr.branch
           # usee.save()
            curr_user.save()


            curr1_user.save()
            dest_user.save()



            t = Transactions(user_account_number = dest_account_number,dest_account_number = a.accountnumber, amount = transfer_amount , balance_after_transaction = dest_user.balance,
                     transaction_type = Recieved_from, bank = a.bank,branch = a.branch )
           # usee = UserBankAccount.objects.get(account_no = dest_account_number)
           # usee.balance = dest_user.balance
           # usee.save()
            print(t.balance_after_transaction)
            t.save()

        return redirect("transactions:status")
    else:
        form = forms.MoneyTransferForm()
        context = {'form':form}
    return render(request, "transfer.html",context)
def trans(request):
    form = TransactionDateRangeForm(request.GET or None)
    daterange= False
    a = User.objects.get(username=request.session['username'])
    queryset = Transactions.objects.filter(user_account_number = a.accountnumber )

    if form.is_valid():
        form_data = form.cleaned_data

        daterange = form_data.get("daterange")

    if daterange:

        queryset = queryset.filter(timestamp__date__range=daterange)
        print(daterange)
        context = {'object_list': queryset, 'form': TransactionDateRangeForm(request.GET or None)}
        return render(request,'report.html',context)

    context = {'object_list':queryset,'form': TransactionDateRangeForm(request.GET or None)}

    return render(request,'report.html',context)

def status(request):
        try:
            curr_user = Status.objects.get(username=request.session['username'])
        except:

            curr_user = Status()
            curr_user.balance = 200
            curr_user.username = request.session['username']
            a = User.objects.get(username=request.session['username'])
            curr_user.account_no=a.accountnumber
            curr_user.save()
        return render(request, "status.html", {"curr_user": curr_user})

def t_history(request):
    form = TransactionDateRangeForm(request.GET or None)
    daterange = False
    queryset = Transactions.objects.filter(transaction_type=Transfered_to)
    if form.is_valid():
        form_data = form.cleaned_data

        daterange = form_data.get("daterange")

    if daterange:
        queryset = queryset.filter(timestamp__date__range=daterange)
        print(daterange)
        context = {'object_list': queryset, 'form': TransactionDateRangeForm(request.GET or None)}
        return render(request, 't_history.html', context)

    context = {'object_list': queryset, 'form': TransactionDateRangeForm(request.GET or None)}

    return render(request, 't_history.html', context)

def l_history(request):
    form = TransactionDateRangeForm(request.GET or None)
    daterange = False
    queryset = Loans.objects.all()
    if form.is_valid():
        form_data = form.cleaned_data

        daterange = form_data.get("daterange")

    if daterange:

        queryset = queryset.filter(loan_date__range=daterange)
        print(daterange)
        context = {'object_list': queryset, 'form': TransactionDateRangeForm(request.GET or None)}
        return render(request, 'l_history.html', context)

    context = {'object_list': queryset, 'form': TransactionDateRangeForm(request.GET or None)}

    return render(request, 'l_history.html', context)

def loanchart(request):
        qs = Loans.objects.values('loan_required_for').annotate(the_count=Count('loan_required_for'))
        context = {'qs': qs}
        return render(request,'loanchart.html',context)


def transchart(request):
        qs= Transactions.objects.filter(transaction_type="Transfered_to").order_by('timestamp__date').values('timestamp__date').distinct().annotate(sum=Sum('amount'))
        context={'qs':qs}
        return render(request, 'transchart.html', context)


def ds(request):
    #a = User.objects.get(username=request.session['username'])
    #qs = Transactions.objects.filter(user_account_number=a.accountnumber)
    qs = Transactions.objects.filter(transaction_type="Transfered_to")
    x=[x.user_account_number for x in qs]
    print(x)
    y=[y.amount for y in qs]
    chart=get_plot(x,y)
    return render(request,"ds.html",{'chart': chart})