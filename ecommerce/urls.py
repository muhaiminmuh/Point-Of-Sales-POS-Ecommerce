"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from master.views import *
from transaction.views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="beranda.html"), name="beranda"),
    path('kategoribarang', list_kategori, name="kategoribarang"),
    path('barang', list_barang, name="barang"),
    path('brand', list_brand, name="brand"),
    path('operator', list_operator, name="operator"),
    path('penjualan', list_penjualan, name="penjualan"),
    path('pembelian', list_pembelian, name="pembelian"),
    path('admin/kategoribarang/pdf', cetak_kategoribarang, name="cetak_kategoribarang"),
    path('admin/brand/pdf', cetak_brand, name="cetak_brand"),
    path('admin/supplier/pdf', cetak_supplier, name="cetak_supplier"),
    path('admin/operator/pdf', cetak_operator, name="cetak_operator"),
    path('admin/barang/pdf', cetak_barang, name="cetak_barang"),
    path('admin/penjualan/pdf', cetak_penjualan, name="cetak_penjualan"),
    path('admin/pembelian/pdf', cetak_pembelian, name="cetak_pembelian"),
    path('admin/operator/grafik', grafik_operator, name="grafik_operator"),
    path('admin/barang/grafik', grafik_barang, name="grafik_barang"),
    path('admin/supplier/grafik', grafik_supplier, name="grafik_supplier"),
    path('admin/pembelian/grafik', grafik_pembelian, name="grafik_pembelian"),
    path('admin/penjualan/grafik', grafik_penjualan, name="grafik_penjualan"),
]
