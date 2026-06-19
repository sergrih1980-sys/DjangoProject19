
from django.contrib import admin
from django.urls import path, include

import shop_products

urlpatterns = [path("admin/", admin.site.urls),
               path('catalog/', include('catalog.urls')),
               path('', include('catalog.urls')),
               path('blog/', include('blog_app.urls')),
               path('shop_products/', include('shop_products.urls', namespace='shop_products')),
               path('', include('users.urls')),
               ]

