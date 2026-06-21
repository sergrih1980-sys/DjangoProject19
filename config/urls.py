
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('blog/', include('blog_app.urls')),
    path('products/', include('shop_products.urls', namespace='shop_products')),
    path('users/', include('users.urls')),


    path('', TemplateView.as_view(template_name='home.html'), name='home'),


]