from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from account import views as account_views
from products import views as product_views

urlpatterns = [
    path('', account_views.index, name="home" ),

    #App-account
    path('login/', account_views.userLogin, name="login"),
    path('register/', account_views.createUser, name="register"),
    path('account/', account_views.userAccount, name="account"),
    path('logout', account_views.userLogout, name="logout"),
    path('admin/', admin.site.urls),

    #App-product
    path('product/', product_views.productPage, name='products'),

    #Password Reset Email
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="reset_password_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="reset_password_confirm"),
    path('reset_password_completed/', auth_views.PasswordResetCompleteView.as_view(), name="reset_password_complete")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

