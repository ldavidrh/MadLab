"""madlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.pages import views

from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cliente/', include('apps.clientes.urls', namespace = 'clientes')),
    path('gerente/', include('apps.usuarios.urls', namespace = 'gerentes')),
    path('productos/', include('apps.productos.urls', namespace='productos')),
    path('categorias/', include('apps.categorias.urls', namespace='categorias')),
    path('subcategorias/', include('apps.subcategorias.urls', namespace='subcategorias')),
    path('almacenes/', include('apps.almacenes.urls', namespace='almacenes')),
    path('inventario/', include('apps.inventario.urls', namespace='inventario')),
    path('descuentos/', include('apps.descuentos.urls', namespace = 'descuentos')),
    path('carritos/', include('apps.carritos.urls', namespace = 'carritos')),
    path('reportes/', include('apps.reportes.urls', namespace = 'reportes')),
    path('facturas/', include('apps.facturas.urls', namespace = 'facturas')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
