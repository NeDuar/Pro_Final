from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from products.views import *
from reportes.views import pdflogin, pdfattempts,pdfinventario,pdfventas
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

urlpatterns = [
    path('', LoginView.as_view(template_name='autenticacion/acceder.html'), name='acceder'),
    path('admin/', admin.site.urls),
    path('acceder/', LoginView.as_view(template_name='autenticacion/acceder.html'), name='acceder'),
    path('logout/', LogoutView.as_view(template_name='autenticacion/acceder.html'), name='logout'),
    path('autenticacion/', include('autenticacion.urls')),
    path('products/', listado_productos, name='products'),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls'), name='products'),

    path('reporte-login/', pdflogin, name='pdflogin'),
    path('reporte-intentos/', pdfattempts, name='intentos'),
    path('reporte-inventario/', pdfinventario, name='inventario'),
    path('reporte-ventas/', pdfventas, name='pdfventas'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
