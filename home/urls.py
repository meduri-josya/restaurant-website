from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('administration/', views.administration, name='administration'),
    path('contact/', views.contact, name='contact'),
]