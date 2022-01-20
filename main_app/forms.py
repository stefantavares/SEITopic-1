from django.forms import ModelForm
from .models import OrderDetail, Profile, Review

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['street_address', 'city', 'state', 'zipcode']

class OrderDetailForm(ModelForm):
  class Meta:
    model = OrderDetail
    fields=['quantity']

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['rating', 'review_text']