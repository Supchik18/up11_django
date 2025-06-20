from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.decorators import method_decorator
from .models import Category, Manufacturer, Material, Product, Customer, Order, OrderItem, Review
from .forms import CategoryForm, ManufacturerForm, MaterialForm, ProductForm, CustomerForm, OrderForm, OrderItemForm, ReviewForm

@permission_required('manager')
def manager_home(request):
    return render(request, 'manager_home.html')

@method_decorator(permission_required('manager.view_category'), name='dispatch')
class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        sort = self.request.GET.get('sort', 'name')
        if sort in ['name', '-name']:
            queryset = queryset.order_by(sort)
        return queryset

@method_decorator(permission_required('manager.view_category'), name='dispatch')
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

@method_decorator(permission_required('manager.add_category'), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

@method_decorator(permission_required('manager.change_category'), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'
    success_url = reverse_lazy('category_list')

@method_decorator(permission_required('manager.delete_category'), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

@method_decorator(permission_required('manager.view_manufacturer'), name='dispatch')
class ManufacturerListView(ListView):
    model = Manufacturer
    template_name = 'manufacturer/manufacturer_list.html'
    context_object_name = 'manufacturers'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        sort = self.request.GET.get('sort', 'name')
        if sort in ['name', '-name', 'country', '-country']:
            queryset = queryset.order_by(sort)
        return queryset

@method_decorator(permission_required('manager.view_manufacturer'), name='dispatch')
class ManufacturerDetailView(DetailView):
    model = Manufacturer
    template_name = 'manufacturer/manufacturer_detail.html'
    context_object_name = 'manufacturer'

@method_decorator(permission_required('manager.add_manufacturer'), name='dispatch')
class ManufacturerCreateView(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'manufacturer/manufacturer_form.html'
    success_url = reverse_lazy('manufacturer_list')

@method_decorator(permission_required('manager.change_manufacturer'), name='dispatch')
class ManufacturerUpdateView(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'manufacturer/manufacturer_form.html'
    success_url = reverse_lazy('manufacturer_list')

@method_decorator(permission_required('manager.delete_manufacturer'), name='dispatch')
class ManufacturerDeleteView(DeleteView):
    model = Manufacturer
    template_name = 'manufacturer/manufacturer_confirm_delete.html'
    success_url = reverse_lazy('manufacturer_list')

@method_decorator(permission_required('manager.view_material'), name='dispatch')
class MaterialListView(ListView):
    model = Material
    template_name = 'material/material_list.html'
    context_object_name = 'materials'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        sort = self.request.GET.get('sort', 'name')
        if sort in ['name', '-name']:
            queryset = queryset.order_by(sort)
        return queryset

@method_decorator(permission_required('manager.view_material'), name='dispatch')
class MaterialDetailView(DetailView):
    model = Material
    template_name = 'material/material_detail.html'
    context_object_name = 'material'

class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material/material_form.html'
    success_url = reverse_lazy('material_list')

class MaterialUpdateView(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'material/material_form.html'
    success_url = reverse_lazy('material_list')

class MaterialDeleteView(DeleteView):
    model = Material
    template_name = 'material/material_confirm_delete.html'
    success_url = reverse_lazy('material_list')

@method_decorator(permission_required('manager.view_product'), name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        sort = self.request.GET.get('sort', 'name')
        if sort in ['name', '-name', 'price', '-price']:
            queryset = queryset.order_by(sort)
        return queryset

@method_decorator(permission_required('manager.view_product'), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

@method_decorator(permission_required('manager.add_product'), name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product_list')

@method_decorator(permission_required('manager.change_product'), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product_list')

@method_decorator(permission_required('manager.delete_product'), name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

@method_decorator(permission_required('manager.view_customer'), name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    context_object_name = 'customers'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(email__icontains=search_query)
        sort = self.request.GET.get('sort', 'first_name')
        if sort in ['first_name', '-first_name', 'email', '-email']:
            queryset = queryset.order_by(sort)
        return queryset

@method_decorator(permission_required('manager.view_customer'), name='dispatch')
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    context_object_name = 'customer'

@method_decorator(permission_required('manager.add_customer'), name='dispatch')
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_form.html'
    success_url = reverse_lazy('customer_list')

@method_decorator(permission_required('manager.change_customer'), name='dispatch')
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer/customer_form.html'
    success_url = reverse_lazy('customer_list')

@method_decorator(permission_required('manager.delete_customer'), name='dispatch')
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')

@method_decorator(permission_required('manager.view_order'), name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        sort = self.request.GET.get('sort', '-created_at')
        if sort in ['created_at', '-created_at', 'total_price', '-total_price']:
            queryset = queryset.order_by(sort)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order()
        return context

@method_decorator(permission_required('manager.view_order'), name='dispatch')
class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'

@method_decorator(permission_required('manager.add_order'), name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')

@method_decorator(permission_required('manager.change_order'), name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order_list')

@method_decorator(permission_required('manager.delete_order'), name='dispatch')
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

@method_decorator(permission_required('manager.view_orderitem'), name='dispatch')
class OrderItemListView(ListView):
    model = OrderItem
    template_name = 'order_item/order_item_list.html'
    context_object_name = 'order_items'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(product__name__icontains=search_query)
        sort = self.request.GET.get('sort', 'quantity')
        if sort in ['quantity', '-quantity', 'price', '-price']:
            queryset = queryset.order_by(sort)
        return queryset

@method_decorator(permission_required('manager.view_orderitem'), name='dispatch')
class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'order_item/order_item_detail.html'
    context_object_name = 'order_item'

@method_decorator(permission_required('manager.add_orderitem'), name='dispatch')
class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'order_item/order_item_form.html'
    success_url = reverse_lazy('order_item_list')

@method_decorator(permission_required('manager.change_orderitem'), name='dispatch')
class OrderItemUpdateView(UpdateView):
    model = OrderItem
    form_class = OrderItemForm
    template_name = 'order_item/order_item_form.html'
    success_url = reverse_lazy('order_item_list')

@method_decorator(permission_required('manager.delete_orderitem'), name='dispatch')
class OrderItemDeleteView(DeleteView):
    model = OrderItem
    template_name = 'order_item/order_item_confirm_delete.html'
    success_url = reverse_lazy('order_item_list')

@method_decorator(permission_required('manager.view_review'), name='dispatch')
class ReviewListView(ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        queryset = super().get_queryset()
        rating = self.request.GET.get('rating')
        if rating:
            queryset = queryset.filter(rating=rating)
        sort = self.request.GET.get('sort', '-created_at')
        if sort in ['rating', '-rating', 'created_at', '-created_at']:
            queryset = queryset.order_by(sort)
        return queryset

@method_decorator(permission_required('manager.view_review'), name='dispatch')
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/review_detail.html'
    context_object_name = 'review'

@method_decorator(permission_required('manager.add_review'), name='dispatch')
class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

@method_decorator(permission_required('manager.change_review'), name='dispatch')
class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/review_form.html'
    success_url = reverse_lazy('review_list')

@method_decorator(permission_required('manager.delete_review'), name='dispatch')
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')