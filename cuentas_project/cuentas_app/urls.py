from django.urls import path
from cuentas_app import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/create/', views.cliente_create, name='cliente_create'),
    path('clientes/<str:cedula>/', views.cliente_detail, name='cliente_detail'),
    path('clientes/<str:cedula>/update/', views.cliente_update, name='cliente_update'),
    path('clientes/<str:pk>/delete/', views.cliente_delete, name='cliente_delete'),
    
]