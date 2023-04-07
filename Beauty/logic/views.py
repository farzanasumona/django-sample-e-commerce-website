import sys
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db.models import F, Sum
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from logic.models import Brand, Product, Order, OrderProduct, Contact


def home(request):
    return render(request, 'home.html')

def sign(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('sign_in')
    else:
        form = UserCreationForm()
        return render(request, 'sign.html', {'form': form})


def forgot(request):
    if request.user.is_authenticated:
        return redirect('sign_in')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Please create an account...."))
            return redirect('sign_in')
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'sign_in.html', {'form': form})


def profile(request):
    if request.user.is_authenticated:
        current_user = request.user
        information = User.objects.get(username=current_user)
        return render(request, 'profile.html', {'information': information})


def contact(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        comment = request.POST['comment']
        current_user = request.user
        contact = Contact(username=username, email=email, comment=comment, user=current_user)
        contact.save()
        messages.success(request, ("Your massage is sent...."))
        return render(request, 'contact.html')

    else:
        return render(request, 'contact.html')


def brand(request):
    bd = Brand.objects.all()
    return render(request, 'brand.html', {'bd': bd})

def sign_out(request):
    logout(request)
    messages.success(request, ("You are now loggedout......."))
    return render(request, 'home.html')

def view(request, id):
    brand = Brand.objects.get(id=id)
    products = brand.products.all
    return render(request, 'view.html', {'products': products})

def order(request):
    if request.method != 'POST':
        return redirect('cart')
    if request.user.is_authenticated:
        # insert into order table
        product_id = request.POST['product_id']
        product = Product.objects.get(id=product_id)
        current_user = request.user
        my_order = Order.objects.filter(user=current_user, is_complete=False).first()
        if my_order is None:
            my_order = Order(total_price=product.price, user=current_user)
        else:
            new_total_price = getattr(my_order, 'total_price') + product.price
            setattr(my_order, 'total_price', new_total_price)
        my_order.save()
        #insert into orderproduct table
        order_product = OrderProduct(order=my_order, product=product)
        order_product.save()
        order = Order.objects.filter(user=current_user, is_complete=False).first()
        orderProducts = OrderProduct.objects.filter(order=order)
        return render(request, 'cart.html', {'orderProducts': orderProducts})
    else:
        return render(request, 'sign_in.html')


def cart(request):
    if request.user.is_authenticated:
        current_user = request.user
        order = Order.objects.filter(user=current_user, is_complete=False).first()
        orderProducts = OrderProduct.objects.filter(order=order)
        return render(request, 'cart.html', {'orderProducts': orderProducts})

def remove(request, id):
    order_product = OrderProduct.objects.filter(id=id).first()
    order = order_product.order
    product = order_product.product
    new_total_price = getattr(order, 'total_price') - product.price
    setattr(order, 'total_price', new_total_price)
    order.save()
    order_product.delete()
    order_product_count = OrderProduct.objects.filter(order_id=order.id).count()
    if order_product_count == 0:
        order.delete()
        return render(request, 'home.html')
    orderProducts = OrderProduct.objects.filter(order=order)
    return render(request, 'cart.html', {'orderProducts': orderProducts})


def checkout(request):
    current_user = request.user
    order = Order.objects.filter(user=current_user, is_complete=False).first()
    return render(request, 'checkout.html', {'order': order})

def payment(request):
    complete_payment = ['Credit card', 'Debit card', 'PayPal']
    if complete_payment is not None:
        current_user = request.user
        order_complete = Order.objects.filter(user=current_user, is_complete=False).first()
        order_complete.is_complete = True
        order_complete.save()
    messages.success(request, ("Your payment is successful......"))
    return render(request, 'home.html')

def search(request):
    query = request.GET['query']
    bd = Brand.objects.filter(name__icontains=query)
    return render(request, 'brand.html', {'bd': bd})
















