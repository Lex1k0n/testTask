from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Product
from .serializers import ProductSerializer, CreateProductSerializer
from rest_framework.permissions import IsAdminUser


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = (IsAdminUser, )


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
