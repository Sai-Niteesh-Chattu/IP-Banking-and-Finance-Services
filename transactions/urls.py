from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    # path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", views.trans,name="report"),
    # path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("transfer/",views.transfer,name = "transfer"),
    path("status/",views.status,name="status"),
    path("t_history/",views.t_history,name="t_history"),
    path("l_history/",views.l_history,name="l_history"),
    path("transchart/",views.transchart,name="transchart"),
    path("loanchart/",views.loanchart,name="loanchart"),
    path("ds/",views.ds,name="ds"),
]
