from django.contrib import admin
from django.urls import path
from .views import ( 
    manager_home, CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    ManufacturerListView, ManufacturerDetailView, ManufacturerCreateView, ManufacturerUpdateView, ManufacturerDeleteView,
    MaterialListView, MaterialDetailView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView,
    ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    OrderItemListView, OrderItemDetailView, OrderItemCreateView, OrderItemUpdateView, OrderItemDeleteView,
    ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView,
)

urlpatterns = [
    path('', manager_home, name='manager_home.html'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('manufacturers/', ManufacturerListView.as_view(), name='manufacturer_list'),
    path('manufacturers/<int:pk>/', ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('manufacturers/create/', ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('manufacturers/<int:pk>/update/', ManufacturerUpdateView.as_view(), name='manufacturer_update'),
    path('manufacturers/<int:pk>/delete/', ManufacturerDeleteView.as_view(), name='manufacturer_delete'),

    path('materials/', MaterialListView.as_view(), name='material_list'),
    path('materials/<int:pk>/', MaterialDetailView.as_view(), name='material_detail'),
    path('materials/create/', MaterialCreateView.as_view(), name='material_create'),
    path('materials/<int:pk>/update/', MaterialUpdateView.as_view(), name='material_update'),
    path('materials/<int:pk>/delete/', MaterialDeleteView.as_view(), name='material_delete'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    path('orderitems/', OrderItemListView.as_view(), name='order_item_list'),
    path('orderitems/<int:pk>/', OrderItemDetailView.as_view(), name='order_item_detail'),
    path('orderitems/create/', OrderItemCreateView.as_view(), name='order_item_create'),
    path('orderitems/<int:pk>/update/', OrderItemUpdateView.as_view(), name='order_item_update'),
    path('orderitems/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='order_item_delete'),

    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]
