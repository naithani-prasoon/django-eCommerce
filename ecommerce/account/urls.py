from django.urls import path

from . import views

urlpatterns=[
    path('',views.createUser,name="register"),
    path('',views.userLogin, name ="login")
]