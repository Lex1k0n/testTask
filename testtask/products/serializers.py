from abc import ABC
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("title", "author", "price")


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ("title", "author", "price", "start_date")
