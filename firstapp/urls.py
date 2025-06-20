from django.contrib import admin
from django.urls import path
from .views import home, catalog, contact, product, manager_home, login_view, register_view, cart_view, add_to_cart, update_cart, order_history,checkout, logout_view;

urlpatterns = [
    path('', home, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('contact/', contact, name='contact'),
    path('product/<int:pk>', product, name='product'),
    path('manager/', manager_home, name=('manager')),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('update-cart/', update_cart, name='update_cart'),
    path('login/', login_view, name=('login')),
    path('register/', register_view, name=('register')),
    path('orders/', order_history, name='order_history'),
    path('checkout/', checkout, name='checkout'),
    path('logout/', logout_view, name='logout'),
]