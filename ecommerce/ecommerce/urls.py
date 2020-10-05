from django.contrib import admin
from django.urls import path, include

from account import views

urlpatterns = [
    path('', views.index, name="home" ),
    path('login/', views.userLogin, name="login"),
    path('register/', views.createUser, name="register"),
    path('account/', views.userAccount, name="account"),
    path('logout',views.userLogout, name="logout"),
    path('admin/', admin.site.urls),
]
