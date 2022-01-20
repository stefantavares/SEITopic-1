from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('tshirts/', views.tshirts_index, name='tshirts_index'),
    path('tshirts/<int:tshirt_id>/', views.tshirts_detail, name='tshirts_detail'),
    path('tshirts/<int:tshirt_id>/add_tshirt', views.add_tshirt, name = 'add_tshirt'),
    path('tshirts/<int:tshirt_id>/add_review', views.add_review, name='add_review'),
    path('myimages/',views.myimages,name='myimages'),
    path('cart/', views.show_cart, name='show_cart'),
    path('cart/complete/', views.complete_order, name='complete_order'),
    path('cart/updatequantity/<int:order_details_id>/', views.update_quantity, name='update_quantity'),
    path('cart/removeitem/<int:order_details_id>/', views.remove_item, name='remove_item'),
    path('orderhistory/', views.show_orders, name='show_orders'),
    path('orderhistory/cancelorder/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('orderhistory/<int:order_id>/', views.order_detail, name='order_detail')
]