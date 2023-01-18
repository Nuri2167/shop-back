from rest_framework import serializers

from api import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('__all__')

# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)

# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     price = serializers.DecimalField(max_digits=15, decimal_places=2)
#     description = serializers.CharField()
#     amount = serializers.IntegerField()
#     is_active = serializers.BooleanField()
#     categories = CategorySerializer()

