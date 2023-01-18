from django.contrib import admin
from django.urls import path
from api.views import ProductViewSet, CategoryViewSet

urlpatterns = [
    path('products/', ProductViewSet.as_view({'get': 'list'})),
    path('products/<int:pk>', ProductViewSet.as_view({'get': 'retrieve'})),
    path('categories/', CategoryViewSet.as_view({'get': 'list'})),
    path('categories/<int:pk>', CategoryViewSet.as_view({'get': 'retrieve'})),
]
