from django.urls import path
from .views import ContactsView, ProductDetailView, HomeView, ProductListView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('', HomeView.as_view(), name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path(
        'product/<int:product_id>/',
        cache_page(60)(ProductDetailView.as_view()),
        name='product_detail'
    ),
  ]