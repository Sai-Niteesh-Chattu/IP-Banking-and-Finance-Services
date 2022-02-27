from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.Home,name="home"),
    path('logouthome/',views.logouthome,name="logouthome"),
    path('about/',views.about,name="about"),
    path('logoutabout/',views.logoutabout,name="logoutabout"),
    path('ourteam/',views.ourteam,name="ourteam"),
    path('logoutteam/', views.logoutteam, name="logoutteam"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('signup/',views.signup,name="signup"),
    path('banks/',views.banks,name="banks"),
    path('sem/',views.sem,name="sem"),


    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="resetpass.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="resetpass1.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="resetpass3.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="resetpass2.html"),
         name="password_reset_complete"),

    path('changepwd/',views.changepwd,name='changepwd'),

]