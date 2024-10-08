from django.urls import path
from .views import create_subcategories, index

urlpatterns = [
    path('', index, name='index'),
    path('create-subcategories/', create_subcategories, name='create_subcategories'),
]
