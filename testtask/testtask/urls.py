from django.contrib import admin
from django.urls import path, include
from products.views import ProductAPIView, CreateAPIView, ProductViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/v1/productlist', ProductViewSet.as_view({'get': 'list'}), name='product_list'),
    path('api/v1/createproduct', CreateAPIView.as_view(), name='create_product'),
]
