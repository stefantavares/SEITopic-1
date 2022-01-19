from django.forms import ModelForm
from .models import OrderDetail, Profile

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['street_address', 'city', 'state', 'zipcode']

class OrderDetailForm(ModelForm):
  class Meta:
    model= OrderDetail
    fields=['quantity']