from django.urls import path
from . import views

urlpatterns = [
    path('show', views.products, name='products'),
    path('show/<int:product_id>', views.show_product, name='product_show'),
    path('complete', views.complete, name='complete'),
    path('create', views.create_product, name='create'),
    path('product_full', views.product_full, name='full_group'),
]
