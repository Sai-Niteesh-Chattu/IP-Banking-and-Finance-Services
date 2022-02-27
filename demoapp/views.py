from django.shortcuts import render,redirect
from django.http import HttpResponse
from transactions.models import Employee
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def Home(request):
    return render(request,"home.html")
def logouthome(request):
    username=request.session['username']
    return render(request,"logouthome.html",{'username':username})
def banks(request):
    return render(request,"banks.html")
def about(request):
    return render(request,"about.html")
def logoutabout(request):
    username = request.session['username']
    return render(request,"logoutabout.html",{'username':username})
def ourteam(request):
    return render(request,"ourteam.html")
def logoutteam(request):
    username = request.session['username']
    return render(request,"logoutteam.html",{'username':username})
def userlogout(request):
    request.session['username']
    del request.session['username']
    messages.info(request,'User logged out')
    return redirect('userlogin')
def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        flag1=Employee.objects.filter(Q(username=username) & Q(password=password))
        if flag1:
            request.session['username'] = username
            return redirect("transactions:t_history")
        flag = User.objects.filter(Q(username=username) & Q(password=password))
        if flag:
            request.session['username'] = username
            return redirect("logouthome")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect("userlogin")
    return render(request, "login.html")
def signup(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('ifsc_no') and request.POST.get('accno') and request.POST.get('username') and request.POST.get('mail') and request.POST.get('pass'):
            s=User()
            s.accountnumber=request.POST.get('accno')
            s.ifsc_no = request.POST.get('ifsc_no')
            ab = s.ifsc_no
            s.username=request.POST.get('username')
            s.email=request.POST.get('mail')
            s.password=request.POST.get('pass')
            a=User.objects.raw('SELECT * from user_table')
            for p in a:
                if p.accountnumber==s.accountnumber or p.username==s.username or p.email==s.email or p.password==s.password:
                    f=1
                    break
            if (f==1):
                messages.error(request,'User already exists')
                return redirect('userlogin')
            else:
                if ab[0:3] ==  "220":
                    s.bank = "SBI"
                    if ab[3:6] == "000":
                        s.branch = "Guntur"
                    elif ab[3:6] == "001":
                        s.branch = "Vijayawada"
                    elif ab[3:6] == "002":
                        s.branch = "Vizag"
                    elif ab[3:6] == "003":
                        s.branch = "Hyderabad"
                    elif ab[3:6] == "004":
                        s.branch = "Amaravathi"
                    elif ab[3:6] == "005":
                        s.branch = "Kakinada"
                    elif ab[3:6] == "006":
                        s.branch = "Machilipatnam"
                    elif ab[3:6] == "007":
                        s.branch = "Secunderabad"
                elif ab[0:3] == "221":
                    s.bank = "HDFC"
                    if ab[3:6] == "000":
                        s.branch = "Guntur"
                    elif ab[3:6] == "001":
                        s.branch = "Vijayawada"
                    elif ab[3:6] == "002":
                        s.branch = "Vizag"
                    elif ab[3:6] == "003":
                        s.branch = "Hyderabad"
                    elif ab[3:6] == "004":
                        s.branch = "Amaravathi"
                    elif ab[3:6] == "005":
                        s.branch = "Kakinada"
                    elif ab[3:6] == "006":
                        s.branch = "Machilipatnam"
                    elif ab[3:6] == "007":
                        s.branch = "Secunderabad"
                elif ab[0:3] == "222":
                    s.bank = "AXIS"
                    if ab[3:6] == "000":
                        s.branch = "Guntur"
                    elif ab[3:6] == "001":
                        s.branch = "Vijayawada"
                    elif ab[3:6] == "002":
                        s.branch = "Vizag"
                    elif ab[3:6] == "003":
                        s.branch = "Hyderabad"
                    elif ab[3:6] == "004":
                        s.branch = "Amaravathi"
                    elif ab[3:6] == "005":
                        s.branch = "Kakinada"
                    elif ab[3:6] == "006":
                        s.branch = "Machilipatnam"
                    elif ab[3:6] == "007":
                        s.branch = "Secunderabad"
                elif ab[0:3] == "223":
                    s.bank = "CANARA"
                    if ab[3:6] == "000":
                        s.branch = "Guntur"
                    elif ab[3:6] == "001":
                        s.branch = "Vijayawada"
                    elif ab[3:6] == "002":
                        s.branch = "Vizag"
                    elif ab[3:6] == "003":
                        s.branch = "Hyderabad"
                    elif ab[3:6] == "004":
                        s.branch = "Amaravathi"
                    elif ab[3:6] == "005":
                        s.branch = "Kakinada"
                    elif ab[3:6] == "006":
                        s.branch = "Machilipatnam"
                    elif ab[3:6] == "007":
                        s.branch = "Secunderabad"
                elif ab[0:3] == "224":
                    s.bank = "UNION"
                    if ab[3:6] == "000":
                        s.branch = "Guntur"
                    elif ab[3:6] == "001":
                        s.branch = "Vijayawada"
                    elif ab[3:6] == "002":
                        s.branch = "Vizag"
                    elif ab[3:6] == "003":
                        s.branch = "Hyderabad"
                    elif ab[3:6] == "004":
                        s.branch = "Amaravathi"
                    elif ab[3:6] == "005":
                        s.branch = "Kakinada"
                    elif ab[3:6] == "006":
                        s.branch = "Machilipatnam"
                    elif ab[3:6] == "007":
                        s.branch = "Secunderabad"
                else:
                    messages.error(request, 'We are not connected with your bank')
                    return redirect('userlogin')

                s.save()
                messages.success(request, 'Account was created for ' + s.username)
                return redirect('userlogin')
    return render(request, "signup.html")

def changepwd(request):
    if request.method == 'POST':
        opwd = request.POST['opwd']
        npwd = request.POST['npwd']
        username = request.POST['username']
        flag = User.objects.filter(Q(username__iexact=username) & Q(password__iexact=opwd))
        if flag:
            User.objects.filter(username=username).update(password=npwd)
            messages.info(request, 'Password updated succesfully')
            return redirect('userlogin')
        else:
            messages.error(request, 'Please check the password')
            return redirect('userlogin')
    return render(request, 'changepwd.html')

def sem(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = StudentForm()
    return render(request, 'sem.html', {'form': form})