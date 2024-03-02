from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=50, default='admin')
    starttime = serializers.DateTimeField()
    price = serializers.IntegerField()
    group_count = serializers.IntegerField()
    min_part = serializers.IntegerField(default=1)
    max_part = serializers.IntegerField(default=1)
