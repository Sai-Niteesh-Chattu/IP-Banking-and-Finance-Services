from django.urls import path
from . import views

app_name = "finance"

urlpatterns = [
    path("loans/",views.loanview,name = "loans"),
    path("loanform/",views.loanform,name = "loanform")
]
