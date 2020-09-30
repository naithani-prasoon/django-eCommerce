from django.contrib import admin
from django.urls import path, include

from account import views

urlpatterns = [
    path('', views.index, name="home" ),
    path('login/', views.userLogin, name="login"),
    path('register/', views.createUser, name="register"),
    path('admin/', admin.site.urls),
]
