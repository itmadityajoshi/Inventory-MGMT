from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index, name='index-page'),
    path('staff/', views.staff, name='staff-page'),
    path('product/', views.product, name='product-page'),
    path('order/', views.order, name='order-page'),

]
