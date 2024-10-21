from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('product/<int:pk>', product, name='product'),
    path('contact/', contact, name='contact'),
]