from django.urls import path
from .views import ContactsView, ProductDetailView, HomeView, ProductListView


urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),

  ]