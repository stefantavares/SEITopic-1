import os 
import json
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Tshirt

# Create your views here.
def home(request):
  return render(request, 'tshirts/home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def tshirts_index(request):
    tshirts = Tshirt.objects.all()
    return render(request, 'tshirts/index.html', {'tshirts': tshirts})

def tshirts_detail(request, tshirt_id):
    tshirt = Tshirt.objects.get(id=tshirt_id)
    return render(request, 'tshirts/detail.html', {
      'tshirt': tshirt
    })

def myimages(request):
    image_path = os.path.dirname(os.path.realpath(__file__))
    images = os.listdir(image_path+"/static/images/logos")
    json_string = json.dumps(images)
    return HttpResponse(json_string)
