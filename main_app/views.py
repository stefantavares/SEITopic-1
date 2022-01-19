import os 
import json
import profile
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Tshirt, Order, OrderDetail
from .forms import ProfileForm, OrderDetailForm
from datetime import date
# Create your views here.
def home(request):
  return render(request, 'tshirts/home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    profile_form = ProfileForm(request.POST)
    if form.is_valid() and profile_form.is_valid():
      # This will add the user to the database
      user = form.save()
      profile = profile_form.save(commit=False)
      profile.user = user
      profile.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('tshirts_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  profile_form = ProfileForm()
  context = {'form': form, 'profile_form': profile_form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def tshirts_index(request):
    tshirts = Tshirt.objects.all()
    return render(request, 'tshirts/index.html', {'tshirts': tshirts})

def tshirts_detail(request, tshirt_id):
    tshirt = Tshirt.objects.get(id=tshirt_id)
    form= OrderDetailForm()
    return render(request, 'tshirts/detail.html', {
      'tshirt': tshirt, 'form': form
    })

def myimages(request):
    image_path = os.path.dirname(os.path.realpath(__file__))
    images = os.listdir(image_path+"/static/images/logos")
    json_string = json.dumps(images)
    return HttpResponse(json_string)

@login_required
def add_tshirt(request, tshirt_id):
  tshirt = Tshirt.objects.get(id=tshirt_id)
  if request.user.profile.order_set.filter(complete=False).count():
    order = request.user.profile.order_set.get(complete=False)
    order_form = OrderDetailForm(request.POST)
    if order_form.is_valid():
      if OrderDetail.objects.filter(order=order, tshirt=tshirt).count():
        order_details = OrderDetail.objects.get(order=order, tshirt=tshirt)
        order_details.quantity += order_form.save(commit=False).quantity
        order_details.save()
        order.total_cost += order_form.save(commit=False).quantity*tshirt.price
        order.save()
        return redirect('show_cart')
      order_details = order_form.save(commit=False)
      order_details.order = order
      order_details.tshirt = tshirt
      order_details.save()
      order.total_cost += order_details.quantity*tshirt.price
      order.save()
      return redirect('show_cart')
  order = Order.objects.create(date = date.today(), user= request.user.profile)
  order_form = OrderDetailForm(request.POST)
  if order_form.is_valid():
    order_details = order_form.save(commit=False)
    order_details.order = order
    order_details.tshirt = tshirt
    order_details.save()
    order.total_cost += order_details.quantity*tshirt.price
    order.save()
    return redirect('show_cart')

@login_required    
def show_cart(request):
  user = request.user
  if user.profile.order_set.filter(complete=False).count():
    order = request.user.profile.order_set.get(complete=False)
    order_details = OrderDetail.objects.filter(order=order)
    return render(request, 'tshirts/cart.html', {'order': order, 'order_details': order_details})
  order = Order.objects.create(date = date.today(), user= request.user.profile)
  order_details = OrderDetail.objects.filter(order=order)
  return render(request, 'tshirts/cart.html', {'order': order, 'order_details': order_details})

@login_required
def complete_order(request):
   order = request.user.profile.order_set.get(complete=False)
   order.complete = True
   order.save()
   return redirect('show_orders')

@login_required
def show_orders(request):
  user = request.user
  orders = user.profile.order_set.filter(complete=True)
  return render(request, 'tshirts/orderhistory.html', {'user': user, 'orders': orders })

@login_required
def update_quantity(request, order_details_id):
  order_details = OrderDetail.objects.get(id=order_details_id)
  update_form = OrderDetailForm(request.POST)
  order_details.order.total_cost += order_details.tshirt.price*(update_form.save(commit=False).quantity - order_details.quantity)
  order_details.order.save()
  order_details.quantity = update_form.save(commit=False).quantity
  order_details.save()
  return redirect('show_cart')

@login_required
def remove_item(request, order_details_id):
  order_details = OrderDetail.objects.get(id=order_details_id)
  order_details.order.total_cost -= order_details.quantity*order_details.tshirt.price
  order_details.order.save()
  order_details.delete()
  return redirect('show_cart')

@login_required
def cancel_order(request, order_id):
  order = Order.objects.get(id=order_id)
  order.delete()
  return redirect('show_orders')

@login_required
def order_detail(request, order_id):
  order = Order.objects.get(id=order_id)
  order_details = OrderDetail.objects.filter(order = order)
  return render(request, 'tshirts/orderdetail.html', {'order': order, 'order_details': order_details})


