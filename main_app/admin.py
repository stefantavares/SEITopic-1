from django.contrib import admin
from .models import Tshirt, Profile, Order, OrderDetail, Review

# Register your models here.
admin.site.register(Tshirt)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Review)