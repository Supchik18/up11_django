from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, CustomerForm
from django.http import JsonResponse
from manager.models import Product, Order, OrderItem, Customer
import json

# Create your views here.
def home(request: WSGIRequest):
    return render(request, 'home.html')

def contact(request: WSGIRequest):
    return render(request, 'contact.html')

@login_required
def catalog(request: WSGIRequest):
    product = Product.objects.all()
    return render(request, 'catalog.html', { 'product': product })

@login_required
def product(request: WSGIRequest, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', { 'product': product })

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/')
                return redirect(next_url)
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('/')
        return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        print(product_id, quantity)
        product = get_object_or_404(Product, pk=product_id)
        if quantity > product.stock or quantity < 1:
            return JsonResponse({'status': 'error', 'message': 'Недопустимое количество'}, status=400)
        cart = request.COOKIES.get('cart', '{}')
        cart_data = json.loads(cart)
        cart_data[product_id] = cart_data.get(product_id, 0) + quantity
        response = JsonResponse({'status': 'success', 'cart': cart_data})
        response.set_cookie('cart', json.dumps(cart_data))
        return response
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def cart_view(request):
    cart = request.COOKIES.get('cart', '{}')
    cart_data = json.loads(cart)
    cart_items = []
    total = 0
    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, pk=product_id)
        if quantity > product.stock:
            quantity = product.stock
            cart_data[product_id] = quantity
            response = JsonResponse({'status': 'updated', 'cart': cart_data})
            response.set_cookie('cart', json.dumps(cart_data))
            return response
        item_total = product.price * quantity
        total += item_total
        cart_items.append({'product': product, 'quantity': quantity, 'total': item_total})
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart = request.COOKIES.get('cart', '{}')
        cart_data = json.loads(cart)
        product = get_object_or_404(Product, pk=product_id)
        if quantity > product.stock:
            return JsonResponse({'status': 'error', 'message': 'Превышен остаток на складе'}, status=400)
        if quantity > 0:
            cart_data[product_id] = quantity
        elif product_id in cart_data:
            del cart_data[product_id]
        response = JsonResponse({'status': 'success', 'cart': cart_data})
        response.set_cookie('cart', json.dumps(cart_data))
        return response
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def checkout(request):
    cart = json.loads(request.COOKIES.get('cart', '{}'))
    if request.method == 'POST' and cart:
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            user = request.user
            customer, created = Customer.objects.get_or_create(
                email=user.email,
                defaults={
                    'first_name': customer_form.cleaned_data['first_name'],
                    'last_name': customer_form.cleaned_data['last_name'],
                    'phone': customer_form.cleaned_data['phone'],
                    'address': customer_form.cleaned_data['address'],
                }
            )
            if not created:
                customer.first_name = customer_form.cleaned_data['first_name']
                customer.last_name = customer_form.cleaned_data['last_name']
                customer.phone = customer_form.cleaned_data['phone']
                customer.address = customer_form.cleaned_data['address']
                customer.save()

            total_price = 0
            order = Order.objects.create(customer=customer, total_price=0)
            for product_id, quantity in cart.items():
                product = get_object_or_404(Product, pk=product_id)
                if quantity > product.stock:
                    quantity = product.stock
                item_total = product.price * quantity
                total_price += item_total
                OrderItem.objects.create(order=order, product=product, quantity=quantity, price=product.price)
            order.total_price = total_price
            order.save()
            response = redirect('order_history')
            response.delete_cookie('cart')
            return response
        else:
            return render(request, 'checkout.html', {'form': customer_form})
    else:
        user = request.user
        customer, created = Customer.objects.get_or_create(
            email=user.email,
            defaults={
                'first_name': user.first_name or user.username,
                'last_name': user.last_name or '',
                'phone': '',
                'address': ''
            }
        )
        form = CustomerForm(instance=customer)
        return render(request, 'checkout.html', {'form': form})

@login_required
def order_history(request):
    orders = Order.objects.filter(customer__email=request.user.email).prefetch_related('items')
    return render(request, 'order_history.html', {'orders': orders})


def manager_home(request: WSGIRequest):
    return render(request, 'manager_home.html')
