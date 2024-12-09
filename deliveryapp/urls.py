
from django.contrib import admin
from django.urls import path
from deliveryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('service/', views.service, name='service'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('quote/', views.quote, name='quote'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.accounts, name='accounts'),
    path('', views.register, name='register'),
    path('login/', views.index, name='login'),
    path('accounts/login/', views.index, name='accounts_login'),
]

