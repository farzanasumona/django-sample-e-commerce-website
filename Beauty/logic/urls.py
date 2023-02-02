from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from logic import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('brand', views.brand, name='brand'),
    path('sign', views.sign, name='sign'),
    path('forgot', views.forgot, name='forgot'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('profile', views.profile, name='profile'),
    path('view/<id>/', views.view, name='view'),
    path('order', views.order, name='order'),
    path('cart', views.cart, name='cart'),
    path('remove/<id>/', views.remove, name='remove'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', views.payment, name='payment'),
    path('search', views.search, name='search'),


]
