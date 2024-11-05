from django.contrib import admin
from django.urls import path
from dummy import views

urlpatterns = [
    path('',views.home, name='home'),
    # path('home/',views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('logout/',views.logoutPage, name='logout')
]