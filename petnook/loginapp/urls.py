from django.contrib import admin
from django.urls import path,include
from loginapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration/',views.customer_register,name='registration'),
    path('sellerreg/',views.seller_register,name='seller_register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    
    path('landing/',views.landing,name='landing'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    # path('profile/',views.profile,name='profile')
    path('accounts/',include('allauth.urls')),
  
    
]
