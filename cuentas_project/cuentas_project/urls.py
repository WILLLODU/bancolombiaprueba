from django.contrib import admin
from django.urls import path, include
from cuentas_app.views import cliente_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cliente_list, name='home'),  # Utiliza cliente_list en lugar de views.cliente_list
    path('clientes/', include('cuentas_app.urls')),
]
