from django.urls import path
from . import views
from .views import ProductsByCategoryView

app_name = 'shop_products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/edit/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('', ProductsByCategoryView.as_view(), name='products_all'),
    path('category/<int:category_id>/', ProductsByCategoryView.as_view(), name='products_by_category'),
]