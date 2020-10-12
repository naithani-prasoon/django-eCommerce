from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns=[
    path('', views.index,name="home"),
    path('',views.createUser,name="register"),
    path('',views.userLogin, name ="login"),
    path('logout',views.userLogout, name="logout"),
    path('',views.userLogin, name ="account"),

    # Password Reset Email
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="reset_password_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="reset_password_confirm"),
    path('reset_password_completed/', auth_views.PasswordResetCompleteView.as_view(), name="reset_password_complete")

]