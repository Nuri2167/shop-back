from django.shortcuts import render, get_list_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(ViewSet):

    def list(request, *args, **kwargs):
        model = Product.objects.all()
        serializer = ProductSerializer(model, many=True)

        return Response(serializer.data)

    def retrieve(request, pk=None):
        model = get_list_or_404(Product.objects.all(), pk=pk)
        serializer = ProductSerializer(model, many=True)

        return Response(serializer.data)


class CategoryViewSet(ViewSet):

    @staticmethod
    def list(request, *args, **kwargs):
        model = Category.objects.all()
        serializer = CategorySerializer(model, many=True)

        return Response(serializer.data)

    @staticmethod
    def retrieve(request, pk=None):
        model = get_list_or_404(Category.objects.all(), pk=pk)
        serializer = CategorySerializer(model, many=True)

        return Response(serializer.data)

# Create your views here.
