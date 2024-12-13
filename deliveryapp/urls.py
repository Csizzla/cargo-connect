
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
    path('', views.register, name='register'),
    path('login/', views.index, name='login'),
    path('account/', views.account, name='account'),
    path('accounts/', views.accept, name='accounts'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),



]

