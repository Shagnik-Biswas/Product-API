from django.urls import path
from .views import ProductView, ProductPopularityView

urlpatterns = [
    # CRUD operations for products
    # GET: List products or search, POST: Create product
    path('products/', ProductView.as_view(), name='product-list-create'),

    # GET: Retrieve product by ID or name, PUT: Update product, DELETE: Delete product
    path('products/<str:product_id>/', ProductView.as_view(), name='product-detail-update-delete'),

    # Calculate product popularity
    # GET: Calculate popularity based on sales
    path('products/<str:product_id>/popularity/', ProductPopularityView.as_view(), name='product-popularity'),
]
